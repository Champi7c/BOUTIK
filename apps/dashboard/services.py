from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta

from apps.orders.models import Order
from apps.store.models import Product, Category, ProductReview, Banner
from django.contrib.auth.models import User

LOW_STOCK_THRESHOLD = 5
CANCELLED_STATUS = 'cancelled'
ACTIVE_ORDER_STATUSES = ['confirmed', 'shipped', 'delivered']


def restore_order_stock(order):
    """Remet le stock en place lors de l'annulation d'une commande."""
    for item in order.items.select_related('product'):
        product = item.product
        product.stock += item.quantity
        product.sales_count = max(0, product.sales_count - item.quantity)
        product.save(update_fields=['stock', 'sales_count'])


def get_dashboard_stats():
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)

    total_orders = Order.objects.count()
    orders_today = Order.objects.filter(created_at__date=today).count()
    orders_week = Order.objects.filter(created_at__date__gte=week_ago).count()
    revenue_month = Order.objects.filter(
        created_at__date__gte=month_ago,
        status__in=ACTIVE_ORDER_STATUSES,
    ).aggregate(total=Sum('total'))['total'] or 0

    status_counts = {
        s['status']: s['count']
        for s in Order.objects.values('status').annotate(count=Count('id'))
    }

    return {
        'total_products': Product.objects.count(),
        'active_products': Product.objects.filter(is_active=True).count(),
        'total_categories': Category.objects.filter(is_active=True).count(),
        'total_customers': User.objects.filter(is_staff=False).count(),
        'pending_orders': Order.objects.filter(status='pending').count(),
        'low_stock_count': Product.objects.filter(is_active=True, stock__lte=LOW_STOCK_THRESHOLD).count(),
        'out_of_stock_count': Product.objects.filter(is_active=True, stock=0).count(),
        'total_reviews': ProductReview.objects.count(),
        'active_banners': Banner.objects.filter(is_active=True).count(),
        'total_orders': total_orders,
        'orders_today': orders_today,
        'orders_week': orders_week,
        'revenue_month': revenue_month,
        'status_counts': status_counts,
        'recent_orders': Order.objects.select_related('user').order_by('-created_at')[:8],
        'low_stock': Product.objects.filter(is_active=True, stock__lte=LOW_STOCK_THRESHOLD).order_by('stock')[:10],
        'top_products': Product.objects.filter(is_active=True).order_by('-sales_count')[:5],
    }
