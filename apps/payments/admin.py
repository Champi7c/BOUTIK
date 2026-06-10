from django.contrib import admin
from django.utils.html import format_html
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'provider', 'amount_display', 'status_badge', 'created_at')
    list_filter = ('status', 'provider', 'created_at')
    search_fields = ('order__order_number', 'transaction_id', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')

    def amount_display(self, obj):
        return format_html('<strong>{:,} FCFA</strong>', int(obj.amount))
    amount_display.short_description = 'Montant'

    def status_badge(self, obj):
        colors = {'pending': '#FFA500', 'completed': '#28a745', 'failed': '#dc3545', 'refunded': '#888'}
        color = colors.get(obj.status, '#888')
        return format_html(
            '<span style="color:{};font-weight:600">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Statut'
