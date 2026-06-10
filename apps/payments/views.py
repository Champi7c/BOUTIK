import json
import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from apps.orders.models import Order
from .models import Payment


# ===== WAVE / ORANGE MONEY =====

@login_required
def initiate_payment(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)

    if request.method == 'POST':
        provider = request.POST.get('provider', 'wave')
        phone = request.POST.get('phone', '')

        payment = Payment.objects.create(
            order=order,
            provider=provider,
            amount=order.grand_total,
            phone_number=phone,
        )

        if provider == 'wave':
            payment_url = f"https://pay.wave.com/m/thiamstreetwear?amount={order.grand_total}"
        elif provider == 'orange_money':
            payment_url = f"https://orangemoney.sn/pay?amount={order.grand_total}"
        else:
            payment.status = 'completed'
            payment.save()
            order.payment_status = 'paid'
            order.status = 'confirmed'
            order.save()
            return redirect('orders:confirmation', order_number=order_number)

        return render(request, 'payments/payment.html', {
            'order': order,
            'payment': payment,
            'payment_url': payment_url,
        })

    return render(request, 'payments/choose_payment.html', {'order': order})


# ===== STRIPE — CARTE BANCAIRE =====

@login_required
def stripe_checkout(request, order_number):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    order = get_object_or_404(Order, order_number=order_number, user=request.user)

    if order.payment_status == 'paid':
        return redirect('orders:confirmation', order_number=order_number)

    success_url = request.build_absolute_uri(
        reverse('payments:stripe_success', args=[order_number])
    ) + '?session_id={CHECKOUT_SESSION_ID}'
    cancel_url = request.build_absolute_uri(
        reverse('payments:stripe_cancel', args=[order_number])
    )

    # Construire les line_items depuis les articles de la commande
    line_items = []
    for item in order.items.all():
        name = item.product.name
        if item.size:
            name += f' — {item.size}'
        if item.color:
            name += f' / {item.color}'
        line_items.append({
            'price_data': {
                'currency': settings.STRIPE_CURRENCY,
                'unit_amount': int(item.unit_price),
                'product_data': {'name': name},
            },
            'quantity': item.quantity,
        })

    # Ajouter les frais de livraison si > 0
    if order.delivery_fee > 0:
        line_items.append({
            'price_data': {
                'currency': settings.STRIPE_CURRENCY,
                'unit_amount': int(order.delivery_fee),
                'product_data': {'name': 'Frais de livraison'},
            },
            'quantity': 1,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
        customer_email=request.user.email or None,
        metadata={'order_number': order_number},
    )

    Payment.objects.update_or_create(
        order=order,
        defaults={
            'provider': 'stripe',
            'amount': order.grand_total,
            'reference': session.id,
            'status': 'pending',
        },
    )

    return redirect(session.url, code=303)


@login_required
def stripe_success(request, order_number):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    session_id = request.GET.get('session_id')

    if session_id:
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            if session.payment_status == 'paid':
                order.payment_status = 'paid'
                order.status = 'confirmed'
                order.save()
                payment = Payment.objects.filter(order=order).first()
                if payment:
                    payment.status = 'completed'
                    payment.transaction_id = session.payment_intent or ''
                    payment.save()
        except stripe.error.StripeError:
            pass

    return redirect('orders:confirmation', order_number=order_number)


@login_required
def stripe_cancel(request, order_number):
    messages.warning(request, 'Paiement par carte annulé. Tu peux réessayer ou choisir un autre moyen de paiement.')
    return render(request, 'payments/stripe_cancel.html', {'order_number': order_number})


# ===== WEBHOOK STRIPE =====

@csrf_exempt
@require_POST
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_number = session.get('metadata', {}).get('order_number')
        if order_number and session.get('payment_status') == 'paid':
            try:
                order = Order.objects.get(order_number=order_number)
                order.payment_status = 'paid'
                order.status = 'confirmed'
                order.save()
                payment = Payment.objects.filter(order=order).first()
                if payment:
                    payment.status = 'completed'
                    payment.transaction_id = session.get('payment_intent', '')
                    payment.save()
            except Order.DoesNotExist:
                pass

    return HttpResponse(status=200)


# ===== WEBHOOK GÉNÉRIQUE (Wave / Orange Money) =====

@csrf_exempt
def payment_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        reference = data.get('reference')
        status = data.get('status')
        try:
            payment = Payment.objects.get(reference=reference)
            if status == 'success':
                payment.status = 'completed'
                payment.order.payment_status = 'paid'
                payment.order.status = 'confirmed'
                payment.order.save()
            else:
                payment.status = 'failed'
            payment.save()
            return JsonResponse({'status': 'ok'})
        except Payment.DoesNotExist:
            return JsonResponse({'error': 'Payment not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
