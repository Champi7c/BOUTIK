from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Connexion admin (séparée du site client)
    path('connexion/', views.admin_login, name='login'),
    path('deconnexion/', views.admin_logout, name='logout'),

    # Vue d'ensemble
    path('', views.dashboard, name='index'),
    path('export/commandes/', views.export_orders_csv, name='export_orders'),

    # Produits
    path('produits/', views.product_list, name='product_list'),
    path('produits/ajouter/', views.product_create, name='product_create'),
    path('produits/<int:pk>/', views.product_edit, name='product_edit'),
    path('produits/<int:pk>/supprimer/', views.product_delete, name='product_delete'),
    path('produits/<int:pk>/toggle/', views.product_toggle, name='product_toggle'),

    # Stock
    path('stock/', views.stock_list, name='stock_list'),

    # Catégories
    path('categories/', views.category_list, name='category_list'),
    path('categories/ajouter/', views.category_create, name='category_create'),
    path('categories/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/supprimer/', views.category_delete, name='category_delete'),

    # Commandes
    path('commandes/', views.order_list, name='order_list'),
    path('commandes/<int:pk>/', views.order_detail, name='order_detail'),

    # Clients
    path('clients/', views.customer_list, name='customer_list'),
    path('clients/<int:pk>/', views.customer_detail, name='customer_detail'),

    # Avis
    path('avis/', views.review_list, name='review_list'),
    path('avis/<int:pk>/supprimer/', views.review_delete, name='review_delete'),

    # Bannières
    path('bannieres/', views.banner_list, name='banner_list'),
    path('bannieres/ajouter/', views.banner_create, name='banner_create'),
    path('bannieres/<int:pk>/', views.banner_edit, name='banner_edit'),
    path('bannieres/<int:pk>/supprimer/', views.banner_delete, name='banner_delete'),

    # Tailles & couleurs
    path('variantes/', views.variants_list, name='variants_list'),
    path('variantes/tailles/<int:pk>/supprimer/', views.size_delete, name='size_delete'),
    path('variantes/couleurs/<int:pk>/supprimer/', views.color_delete, name='color_delete'),
]
