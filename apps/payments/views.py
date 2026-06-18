from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from apps.orders.models import Order
import json


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

        # Simulation — en production, appeler l'API Wave/Orange Money
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


@csrf_exempt
def payment_webhook(request):
    """Webhook pour recevoir les confirmations de paiement."""
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
