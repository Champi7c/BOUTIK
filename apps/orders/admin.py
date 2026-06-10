from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse
import csv
from .models import Order, OrderItem, Cart, CartItem


class OrderItemInline(admin.TabularInline):
    model = Order.items.through
    extra = 0
    verbose_name = 'Article'
    verbose_name_plural = 'Articles'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'unit_price', 'size', 'color')
    readonly_fields = ('subtotal',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number', 'user_name', 'total_display',
        'status', 'status_badge', 'payment_badge', 'delivery_type',
        'created_at'
    )
    list_filter = ('status', 'payment_method', 'delivery_type', 'created_at')
    list_editable = ('status',)
    search_fields = ('order_number', 'user__username', 'user__email', 'phone')
    readonly_fields = ('order_number', 'created_at', 'updated_at', 'grand_total_display')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    actions = ['export_csv', 'mark_confirmed', 'mark_shipped', 'mark_delivered']

    fieldsets = (
        ('Commande', {
            'fields': ('order_number', 'user', 'status', 'notes')
        }),
        ('Livraison', {
            'fields': ('delivery_type', 'delivery_address', 'delivery_fee', 'phone')
        }),
        ('Paiement', {
            'fields': ('payment_method', 'payment_status', 'total', 'grand_total_display')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def user_name(self, obj):
        name = f'{obj.user.first_name} {obj.user.last_name}'.strip() or obj.user.username
        return format_html('<strong>{}</strong><br><small style="color:#888">{}</small>', name, obj.user.email)
    user_name.short_description = 'Client'

    def total_display(self, obj):
        return format_html('<strong>{:,} FCFA</strong>', int(obj.grand_total))
    total_display.short_description = 'Total'

    def grand_total_display(self, obj):
        return f'{int(obj.grand_total):,} FCFA'
    grand_total_display.short_description = 'Total TTC'

    def status_badge(self, obj):
        colors = {
            'pending': '#FFA500',
            'confirmed': '#3b82f6',
            'preparing': '#8b5cf6',
            'shipped': '#06b6d4',
            'delivered': '#28a745',
            'cancelled': '#dc3545',
        }
        color = colors.get(obj.status, '#888')
        return format_html(
            '<span style="background:{};color:white;padding:.2rem .6rem;font-size:.7rem;font-weight:700;letter-spacing:1px;border-radius:2px">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Statut'

    def payment_badge(self, obj):
        color = '#28a745' if obj.payment_status == 'paid' else '#FFA500'
        return format_html(
            '<span style="color:{};font-size:.8rem;font-weight:600">{}</span>',
            color, 'Payé' if obj.payment_status == 'paid' else 'En attente'
        )
    payment_badge.short_description = 'Paiement'

    # Actions groupées
    @admin.action(description='Confirmer les commandes sélectionnées')
    def mark_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} commande(s) confirmée(s).')

    @admin.action(description='Marquer comme expédiées')
    def mark_shipped(self, request, queryset):
        updated = queryset.update(status='shipped')
        self.message_user(request, f'{updated} commande(s) expédiée(s).')

    @admin.action(description='Marquer comme livrées')
    def mark_delivered(self, request, queryset):
        updated = queryset.update(status='delivered')
        self.message_user(request, f'{updated} commande(s) livrée(s).')

    @admin.action(description='Exporter en CSV')
    def export_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="commandes.csv"'
        response.write('\ufeff')
        writer = csv.writer(response, delimiter=';')
        writer.writerow(['N° Commande', 'Client', 'Email', 'Téléphone', 'Total', 'Statut', 'Date'])
        for order in queryset:
            writer.writerow([
                order.order_number,
                order.user.get_full_name() or order.user.username,
                order.user.email,
                order.phone,
                f'{int(order.grand_total)} FCFA',
                order.get_status_display(),
                order.created_at.strftime('%d/%m/%Y %H:%M'),
            ])
        return response
