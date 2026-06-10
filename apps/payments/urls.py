from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    # Wave / Orange Money
    path('payer/<str:order_number>/', views.initiate_payment, name='pay'),
    path('webhook/', views.payment_webhook, name='webhook'),

    # Stripe — carte bancaire Visa / Mastercard
    path('carte/<str:order_number>/', views.stripe_checkout, name='stripe_checkout'),
    path('carte/succes/<str:order_number>/', views.stripe_success, name='stripe_success'),
    path('carte/annule/<str:order_number>/', views.stripe_cancel, name='stripe_cancel'),
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),
]
