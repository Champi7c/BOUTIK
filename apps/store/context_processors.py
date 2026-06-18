from django.conf import settings

from .models import Category, Wishlist
from apps.orders.cart import Cart


def cart_count(request):
    cart = Cart(request)
    return {'cart_count': len(cart), 'cart': cart}


def categories_menu(request):
    categories = Category.objects.filter(is_active=True, parent=None).prefetch_related('children')
    return {'menu_categories': categories}


def wishlist_ids(request):
    if request.user.is_authenticated and not request.user.is_staff:
        ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
        return {'wishlist_ids': set(ids)}
    return {'wishlist_ids': set()}


def boutique_info(request):
    wa = getattr(settings, 'WHATSAPP_URL', f"https://wa.me/{settings.WHATSAPP_NUMBER}")
    return {
        'boutique_name': 'ThiamStreetwear',
        'boutique_tel': settings.BOUTIQUE_TEL,
        'boutique_location': settings.BOUTIQUE_LOCATION,
        'boutique_plus_code': getattr(settings, 'BOUTIQUE_PLUS_CODE', ''),
        'boutique_maps_url': getattr(settings, 'BOUTIQUE_MAPS_URL', ''),
        'boutique_maps_embed': getattr(settings, 'BOUTIQUE_MAPS_EMBED', ''),
        'boutique_horaires': getattr(settings, 'BOUTIQUE_HORAIRES', ''),
        'boutique_whatsapp_url': wa,
        'boutique_instagram_url': settings.INSTAGRAM_URL,
        'boutique_snapchat_url': settings.SNAPCHAT_URL,
        # SEA
        'GTM_ID': getattr(settings, 'GTM_ID', ''),
        'META_PIXEL_ID': getattr(settings, 'META_PIXEL_ID', ''),
        'SITE_URL': getattr(settings, 'SITE_URL', 'https://thiamstreetwear.com'),
    }
