from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from .models import Product, Category, ProductReview, Wishlist, Banner


def home(request):
    banners = Banner.objects.filter(is_active=True)[:3]
    new_products = Product.objects.filter(is_active=True, is_new=True)[:8]
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    popular_products = Product.objects.filter(is_active=True).order_by('-sales_count')[:8]

    # Catégories avec comptage réel (inclut sous-catégories)
    raw_cats = Category.objects.filter(is_active=True, parent=None).exclude(
        name__in=['Nouveautés', 'Soldes']
    )[:4]
    top_categories = []
    for cat in raw_cats:
        cat.total_products = Product.objects.filter(
            is_active=True
        ).filter(
            Q(category=cat) | Q(category__parent=cat)
        ).count()
        top_categories.append(cat)
    context = {
        'banners': banners,
        'new_products': new_products,
        'featured_products': featured_products,
        'popular_products': popular_products,
        'top_categories': top_categories,
        'page': 'home',
    }
    return render(request, 'store/home.html', context)


def product_list(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)

    # Filtres
    category_slug = request.GET.get('categorie')
    price_min = request.GET.get('prix_min')
    price_max = request.GET.get('prix_max')
    size_filter = request.GET.get('taille')
    color_filter = request.GET.get('couleur')
    is_new = request.GET.get('nouveau')
    is_promo = request.GET.get('promo')
    sort = request.GET.get('tri', '-created_at')
    query = request.GET.get('q', '')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(
            Q(category=category) | Q(category__parent=category)
        )
    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)
    if size_filter:
        products = products.filter(sizes__name=size_filter)
    if color_filter:
        products = products.filter(colors__name=color_filter)
    if is_new:
        products = products.filter(is_new=True)
    if is_promo:
        products = products.filter(discount_price__isnull=False)
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    sort_options = {
        'prix_asc': 'price',
        'prix_desc': '-price',
        'nouveau': '-created_at',
        'populaire': '-sales_count',
    }
    products = products.order_by(sort_options.get(sort, '-created_at'))

    context = {
        'products': products,
        'categories': categories,
        'query': query,
        'page': 'catalogue',
    }
    return render(request, 'store/product_list.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    subcategories = category.children.filter(is_active=True)
    products = Product.objects.filter(
        is_active=True
    ).filter(
        Q(category=category) | Q(category__parent=category)
    )

    sort = request.GET.get('tri', '-created_at')
    sort_options = {
        'prix_asc': 'price', 'prix_desc': '-price',
        'nouveau': '-created_at', 'populaire': '-sales_count',
    }
    products = products.order_by(sort_options.get(sort, '-created_at'))

    context = {
        'category': category,
        'subcategories': subcategories,
        'products': products,
        'page': 'catalogue',
    }
    return render(request, 'store/category_detail.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    product.views_count += 1
    product.save(update_fields=['views_count'])

    related = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(id=product.id)[:4]

    reviews = product.reviews.all().order_by('-created_at')
    is_wishlisted = False
    user_review = None

    if request.user.is_authenticated:
        is_wishlisted = Wishlist.objects.filter(
            user=request.user, product=product
        ).exists()
        user_review = reviews.filter(user=request.user).first()

    # Soumettre un avis
    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')
        if rating and not user_review:
            ProductReview.objects.create(
                product=product, user=request.user,
                rating=int(rating), comment=comment
            )
            messages.success(request, 'Votre avis a été publié.')
            return redirect('store:product_detail', slug=slug)

    context = {
        'product': product,
        'related': related,
        'reviews': reviews,
        'is_wishlisted': is_wishlisted,
        'user_review': user_review,
        'page': 'produit',
    }
    return render(request, 'store/product_detail.html', context)


@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product
    )
    if not created:
        wishlist_item.delete()
        action = 'removed'
    else:
        action = 'added'

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'action': action, 'product_id': product_id})
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'store/wishlist.html', {'items': items, 'page': 'wishlist'})


def search(request):
    query = request.GET.get('q', '')
    products = []
    if query:
        products = Product.objects.filter(
            is_active=True
        ).filter(
            Q(name__icontains=query) | Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )[:20]

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = [{
            'id': p.id,
            'name': p.name,
            'price': str(p.current_price),
            'image': p.image.url if p.image else '',
            'url': p.get_absolute_url(),
        } for p in products]
        return JsonResponse({'results': data})

    return render(request, 'store/search.html', {
        'products': products, 'query': query
    })


def contact(request):
    if request.method == 'POST':
        messages.success(
            request,
            'Votre message a bien été envoyé. Nous vous répondrons dans les plus brefs délais.'
        )
        return redirect('store:contact')
    return render(request, 'pages/contact.html', {'page': 'contact'})


def about(request):
    return render(request, 'pages/about.html', {'page': 'a-propos'})
