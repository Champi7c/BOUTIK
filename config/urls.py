from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from apps.store.sitemaps import ProductSitemap, CategorySitemap, StaticSitemap

sitemaps = {
    'produits': ProductSitemap,
    'categories': CategorySitemap,
    'pages': StaticSitemap,
}

def robots_txt(request):
    lines = [
        'User-agent: *',
        'Disallow: /admin/',
        'Disallow: /dashboard/',
        'Disallow: /compte/',
        'Disallow: /paiement/',
        f'Sitemap: {settings.SITE_URL}/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')

def google_verification(request):
    return HttpResponse(
        'google-site-verification: google8c9c3311e3b98289.html',
        content_type='text/html'
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.store.urls')),
    path('', include('apps.orders.urls')),
    path('compte/', include('apps.accounts.urls')),
    path('paiement/', include('apps.payments.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
    path('google8c9c3311e3b98289.html', google_verification),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Personnalisation de l'admin
admin.site.site_header = 'ThiamStreetwear Admin'
admin.site.site_title = 'ThiamSW'
admin.site.index_title = 'Panneau de gestion'
