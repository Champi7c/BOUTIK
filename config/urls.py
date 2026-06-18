from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.store.urls')),
    path('', include('apps.orders.urls')),
    path('compte/', include('apps.accounts.urls')),
    path('paiement/', include('apps.payments.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Personnalisation de l'admin
admin.site.site_header = 'ThiamStreetwear Admin'
admin.site.site_title = 'ThiamSW'
admin.site.index_title = 'Panneau de gestion'
