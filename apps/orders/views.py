from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .cart import Cart
from .models import Order, OrderItem
from apps.store.models import Product, Size, Color
import json


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'orders/cart.html', {'cart': cart, 'page': 'panier'})


@require_POST
def cart_add(request):
    data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
    product_id = data.get('product_id')
    quantity = int(data.get('quantity', 1))
    size = data.get('size', '')
    color = data.get('color', '')

    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart = Cart(request)
    cart.add(product=product, quantity=quantity, size=size, color=color)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': len(cart),
            'cart_total': cart.get_total(),
            'message': f'{product.name} ajouté au panier',
        })
    messages.success(request, f'{product.name} ajouté au panier !')
    return redirect('orders:cart')


@require_POST
def cart_remove(request):
    data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
    key = data.get('key')
    cart = Cart(request)
    cart.remove(key)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_count': len(cart),
            'cart_total': cart.get_total(),
        })
    return redirect('orders:cart')


@require_POST
def cart_update(request):
    data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
    key = data.get('key')
    quantity = int(data.get('quantity', 1))
    cart = Cart(request)

    if key in cart.cart:
        cart.cart[key]['quantity'] = max(1, quantity)
        cart.save()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        item = cart.cart.get(key, {})
        item_total = int(item.get('price', 0)) * item.get('quantity', 0)
        return JsonResponse({
            'success': True,
            'cart_count': len(cart),
            'cart_total': cart.get_total(),
            'item_total': item_total,
        })
    return redirect('orders:cart')


@login_required
def checkout(request):
    cart = Cart(request)
    if cart.is_empty():
        messages.warning(request, 'Votre panier est vide.')
        return redirect('orders:cart')

    if request.method == 'POST':
        delivery_type = request.POST.get('delivery_type', 'livraison')
        delivery_address = request.POST.get('delivery_address', '').strip()
        phone = request.POST.get('phone', '').strip()
        payment_method = request.POST.get('payment_method', 'cash')
        notes = request.POST.get('notes', '')
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()

        if delivery_type == 'livraison' and not delivery_address:
            messages.error(request, 'Veuillez indiquer votre adresse de livraison.')
            return redirect('orders:checkout')

        if not phone:
            messages.error(request, 'Le numéro de téléphone est obligatoire.')
            return redirect('orders:checkout')

        delivery_fee = 1500 if delivery_type == 'livraison' else 0

        # Mettre à jour le profil client
        from apps.accounts.models import Profile
        profile, _ = Profile.objects.get_or_create(user=request.user)
        profile.phone = phone
        if delivery_type == 'livraison':
            profile.address = delivery_address
        profile.save()
        if first_name:
            request.user.first_name = first_name
        if last_name:
            request.user.last_name = last_name
        request.user.save(update_fields=['first_name', 'last_name'])

        # Créer la commande
        order = Order.objects.create(
            user=request.user,
            total=cart.get_total(),
            delivery_type=delivery_type,
            delivery_address=delivery_address,
            delivery_fee=delivery_fee,
            phone=phone,
            payment_method=payment_method,
            notes=notes,
        )

        # Créer les articles
        for item in cart:
            size = Size.objects.filter(name=item.get('size')).first() if item.get('size') else None
            color = Color.objects.filter(name=item.get('color')).first() if item.get('color') else None
            order_item = OrderItem.objects.create(
                product=item['product'],
                quantity=item['quantity'],
                unit_price=item['price'],
                size=size,
                color=color,
            )
            order.items.add(order_item)

            # Décrémenter stock
            product = item['product']
            product.stock = max(0, product.stock - item['quantity'])
            product.sales_count += item['quantity']
            product.save(update_fields=['stock', 'sales_count'])

        order.save()
        cart.clear()

        request.session['last_order_id'] = order.id
        return redirect('orders:confirmation', order_number=order.order_number)

    DELIVERY_FEE = 1500
    from apps.accounts.models import Profile
    profile, _ = Profile.objects.get_or_create(user=request.user)
    context = {
        'cart': cart,
        'cart_total': cart.get_total(),
        'delivery_fee': DELIVERY_FEE,
        'profile': profile,
        'page': 'checkout',
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'orders/confirmation.html', {
        'order': order, 'page': 'confirmation'
    })


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {
        'orders': orders, 'page': 'commandes'
    })


@login_required
def order_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'orders/order_detail.html', {
        'order': order, 'page': 'commande'
    })
