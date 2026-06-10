from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('produits/', views.product_list, name='product_list'),
    path('categorie/<slug:slug>/', views.category_detail, name='category'),
    path('produit/<slug:slug>/', views.product_detail, name='product_detail'),
    path('recherche/', views.search, name='search'),
    path('favoris/', views.wishlist, name='wishlist'),
    path('favoris/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('contact/', views.contact, name='contact'),
    path('a-propos/', views.about, name='about'),
]
