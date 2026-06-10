from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('panier/', views.cart_detail, name='cart'),
    path('panier/ajouter/', views.cart_add, name='cart_add'),
    path('panier/supprimer/', views.cart_remove, name='cart_remove'),
    path('panier/modifier/', views.cart_update, name='cart_update'),
    path('commande/', views.checkout, name='checkout'),
    path('commande/confirmation/<str:order_number>/', views.order_confirmation, name='confirmation'),
    path('mes-commandes/', views.order_list, name='order_list'),
    path('commande/<str:order_number>/', views.order_detail, name='order_detail'),
]
