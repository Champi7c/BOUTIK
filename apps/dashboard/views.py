from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
import csv

from apps.orders.models import Order
from apps.store.models import Product, Category, ProductReview, Banner, Size, Color
from apps.payments.models import Payment

from .forms import (
    ProductForm, CategoryForm, BannerForm, OrderStatusForm,
    StockAdjustForm, SizeForm, ColorForm, CustomerStaffForm,
)
from .services import get_dashboard_stats, restore_order_stock, LOW_STOCK_THRESHOLD
from .decorators import manager_required
from apps.accounts.auth_helpers import authenticate_user, login_account


# ─── CONNEXION ADMIN (séparée du site client) ─────────────────────

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard:index')

    if request.method == 'POST':
        identifier = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate_user(identifier, password, request)

        if user is None:
            messages.error(request, 'Identifiants administrateur incorrects.')
        elif not user.is_staff:
            messages.error(
                request,
                'Ce compte est un compte client. Connectez-vous sur /compte/connexion/'
            )
        elif not user.is_active:
            messages.error(request, 'Compte administrateur désactivé.')
        else:
            login_account(request, user)
            messages.success(request, f'Bienvenue {user.first_name or user.username}.')
            next_url = request.GET.get('next', reverse('dashboard:index'))
            return redirect(next_url)

    return render(request, 'dashboard/login.html')


def admin_logout(request):
    logout(request)
    messages.info(request, 'Session administrateur fermée.')
    return redirect('dashboard:login')


# ─── VUE D'ENSEMBLE ───────────────────────────────────────────────

@manager_required
def dashboard(request):
    return render(request, 'dashboard/index.html', get_dashboard_stats())


@manager_required
def export_orders_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="commandes_brightlooks.csv"'
    response.write('\ufeff')

    writer = csv.writer(response, delimiter=';')
    writer.writerow([
        'N° Commande', 'Client', 'Email', 'Téléphone',
        'Total (FCFA)', 'Frais livraison', 'Statut',
        'Paiement', 'Date',
    ])

    for order in Order.objects.select_related('user').order_by('-created_at'):
        writer.writerow([
            order.order_number,
            f'{order.user.first_name} {order.user.last_name}'.strip() or order.user.username,
            order.user.email,
            order.phone,
            order.total,
            order.delivery_fee,
            order.get_status_display(),
            order.get_payment_method_display(),
            order.created_at.strftime('%d/%m/%Y %H:%M'),
        ])
    return response


# ─── PRODUITS ───────────────────────────────────────────────────────

@manager_required
def product_list(request):
    q = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '')
    stock_filter = request.GET.get('stock', '')

    products = Product.objects.select_related('category').order_by('-created_at')
    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
    if category_id:
        products = products.filter(category_id=category_id)
    if stock_filter == 'low':
        products = products.filter(stock__lte=LOW_STOCK_THRESHOLD)
    elif stock_filter == 'out':
        products = products.filter(stock=0)

    paginator = Paginator(products, 15)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'dashboard/products/list.html', {
        'products': page,
        'categories': Category.objects.filter(is_active=True),
        'q': q,
        'category_id': category_id,
        'stock_filter': stock_filter,
        'total_count': products.count(),
    })


@manager_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        product = form.save()
        messages.success(request, f'Produit « {product.name} » créé avec succès.')
        return redirect('dashboard:product_edit', pk=product.pk)
    return render(request, 'dashboard/products/form.html', {
        'form': form, 'title': 'Ajouter un produit', 'is_create': True,
    })


@manager_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Produit « {product.name} » mis à jour.')
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/products/form.html', {
        'form': form, 'product': product, 'title': 'Modifier le produit', 'is_create': False,
    })


@manager_required
@require_POST
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    name = product.name
    product.delete()
    messages.success(request, f'Produit « {name} » supprimé.')
    return redirect('dashboard:product_list')


@manager_required
@require_POST
def product_toggle(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_active = not product.is_active
    product.save(update_fields=['is_active'])
    state = 'activé' if product.is_active else 'désactivé'
    messages.success(request, f'Produit « {product.name} » {state}.')
    return redirect(request.META.get('HTTP_REFERER') or reverse('dashboard:product_list'))


# ─── STOCK ──────────────────────────────────────────────────────────

@manager_required
def stock_list(request):
    q = request.GET.get('q', '').strip()
    products = Product.objects.select_related('category').order_by('stock', 'name')
    if q:
        products = products.filter(name__icontains=q)

    filter_type = request.GET.get('filter', '')
    if filter_type == 'low':
        products = products.filter(stock__lte=LOW_STOCK_THRESHOLD, stock__gt=0)
    elif filter_type == 'out':
        products = products.filter(stock=0)

    if request.method == 'POST':
        updated = 0
        for key, value in request.POST.items():
            if key.startswith('stock_'):
                try:
                    product_id = int(key.replace('stock_', ''))
                    new_stock = max(0, int(value))
                    Product.objects.filter(pk=product_id).update(stock=new_stock)
                    updated += 1
                except (ValueError, TypeError):
                    pass
        messages.success(request, f'Stock mis à jour pour {updated} produit(s).')
        return redirect('dashboard:stock_list')

    paginator = Paginator(products, 20)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'dashboard/stock/list.html', {
        'products': page,
        'q': q,
        'filter_type': filter_type,
        'low_threshold': LOW_STOCK_THRESHOLD,
        'out_count': Product.objects.filter(stock=0, is_active=True).count(),
        'low_count': Product.objects.filter(stock__lte=LOW_STOCK_THRESHOLD, stock__gt=0, is_active=True).count(),
    })


# ─── CATÉGORIES ─────────────────────────────────────────────────────

@manager_required
def category_list(request):
    categories = Category.objects.select_related('parent').order_by('order', 'name')
    return render(request, 'dashboard/categories/list.html', {'categories': categories})


@manager_required
def category_create(request):
    form = CategoryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        cat = form.save()
        messages.success(request, f'Catégorie « {cat.name} » créée.')
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/categories/form.html', {
        'form': form, 'title': 'Ajouter une catégorie',
    })


@manager_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Catégorie « {category.name} » mise à jour.')
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/categories/form.html', {
        'form': form, 'category': category, 'title': 'Modifier la catégorie',
    })


@manager_required
@require_POST
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if category.products.exists():
        messages.error(request, f'Impossible de supprimer « {category.name} » : des produits y sont liés.')
    else:
        name = category.name
        category.delete()
        messages.success(request, f'Catégorie « {name} » supprimée.')
    return redirect('dashboard:category_list')


# ─── COMMANDES ──────────────────────────────────────────────────────

@manager_required
def order_list(request):
    status = request.GET.get('status', '')
    q = request.GET.get('q', '').strip()

    orders = Order.objects.select_related('user').order_by('-created_at')
    if status:
        orders = orders.filter(status=status)
    if q:
        orders = orders.filter(
            Q(order_number__icontains=q)
            | Q(user__username__icontains=q)
            | Q(user__email__icontains=q)
            | Q(phone__icontains=q)
        )

    paginator = Paginator(orders, 20)
    page = paginator.get_page(request.GET.get('page'))

    counts = {s['status']: s['count'] for s in Order.objects.values('status').annotate(count=Count('id'))}
    status_tabs = [(code, label, counts.get(code, 0)) for code, label in Order.STATUS]

    return render(request, 'dashboard/orders/list.html', {
        'orders': page,
        'status': status,
        'q': q,
        'status_tabs': status_tabs,
        'total_orders': Order.objects.count(),
    })


@manager_required
def order_detail(request, pk):
    order = get_object_or_404(Order.objects.select_related('user'), pk=pk)
    old_status = order.status
    form = OrderStatusForm(request.POST or None, instance=order)

    if request.method == 'POST' and form.is_valid():
        new_status = form.cleaned_data['status']
        if new_status == 'cancelled' and old_status != 'cancelled':
            restore_order_stock(order)
        order = form.save()
        messages.success(request, f'Commande {order.order_number} mise à jour.')
        return redirect('dashboard:order_detail', pk=pk)

    items = order.items.select_related('product', 'size', 'color')
    payment = Payment.objects.filter(order=order).first()

    return render(request, 'dashboard/orders/detail.html', {
        'order': order,
        'items': items,
        'form': form,
        'payment': payment,
    })


# ─── CLIENTS ────────────────────────────────────────────────────────

@manager_required
def customer_list(request):
    q = request.GET.get('q', '').strip()
    customers = User.objects.filter(is_staff=False).select_related('profile').order_by('-date_joined')
    if q:
        customers = customers.filter(
            Q(username__icontains=q) | Q(email__icontains=q)
            | Q(first_name__icontains=q) | Q(last_name__icontains=q)
        )

    paginator = Paginator(customers, 20)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'dashboard/customers/list.html', {
        'customers': page, 'q': q,
    })


@manager_required
def customer_detail(request, pk):
    customer = get_object_or_404(User.objects.select_related('profile'), pk=pk, is_staff=False)
    form = CustomerStaffForm(request.POST or None, instance=customer)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Client « {customer.username} » mis à jour.')
        return redirect('dashboard:customer_detail', pk=pk)

    orders = Order.objects.filter(user=customer).order_by('-created_at')[:10]
    return render(request, 'dashboard/customers/detail.html', {
        'customer': customer, 'form': form, 'orders': orders,
    })


# ─── AVIS ───────────────────────────────────────────────────────────

@manager_required
def review_list(request):
    reviews = ProductReview.objects.select_related('product', 'user').order_by('-created_at')
    paginator = Paginator(reviews, 20)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'dashboard/reviews/list.html', {'reviews': page})


@manager_required
@require_POST
def review_delete(request, pk):
    review = get_object_or_404(ProductReview, pk=pk)
    review.delete()
    messages.success(request, 'Avis supprimé.')
    return redirect('dashboard:review_list')


# ─── BANNIÈRES ──────────────────────────────────────────────────────

@manager_required
def banner_list(request):
    banners = Banner.objects.order_by('order')
    return render(request, 'dashboard/banners/list.html', {'banners': banners})


@manager_required
def banner_create(request):
    form = BannerForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        banner = form.save()
        messages.success(request, f'Bannière « {banner.title} » créée.')
        return redirect('dashboard:banner_list')
    return render(request, 'dashboard/banners/form.html', {
        'form': form, 'title': 'Ajouter une bannière',
    })


@manager_required
def banner_edit(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    form = BannerForm(request.POST or None, request.FILES or None, instance=banner)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Bannière « {banner.title} » mise à jour.')
        return redirect('dashboard:banner_list')
    return render(request, 'dashboard/banners/form.html', {
        'form': form, 'banner': banner, 'title': 'Modifier la bannière',
    })


@manager_required
@require_POST
def banner_delete(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    banner.delete()
    messages.success(request, 'Bannière supprimée.')
    return redirect('dashboard:banner_list')


# ─── TAILLES & COULEURS ─────────────────────────────────────────────

@manager_required
def variants_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_size':
            form = SizeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Taille ajoutée.')
        elif action == 'add_color':
            form = ColorForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Couleur ajoutée.')
        return redirect('dashboard:variants_list')

    return render(request, 'dashboard/variants/list.html', {
        'sizes': Size.objects.order_by('order', 'name'),
        'colors': Color.objects.order_by('name'),
        'size_form': SizeForm(),
        'color_form': ColorForm(),
    })


@manager_required
@require_POST
def size_delete(request, pk):
    Size.objects.filter(pk=pk).delete()
    messages.success(request, 'Taille supprimée.')
    return redirect('dashboard:variants_list')


@manager_required
@require_POST
def color_delete(request, pk):
    Color.objects.filter(pk=pk).delete()
    messages.success(request, 'Couleur supprimée.')
    return redirect('dashboard:variants_list')
