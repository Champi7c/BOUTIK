from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('payer/<str:order_number>/', views.initiate_payment, name='pay'),
    path('webhook/', views.payment_webhook, name='webhook'),
]
