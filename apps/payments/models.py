from django.db import models
from apps.orders.models import Order


class Payment(models.Model):
    PROVIDER_CHOICES = [
        ('wave', 'Wave'),
        ('orange_money', 'Orange Money'),
        ('stripe', 'Carte bancaire (Stripe)'),
        ('paydunya', 'PayDunya'),
        ('cash', 'Espèces'),
    ]
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('completed', 'Complété'),
        ('failed', 'Échoué'),
        ('refunded', 'Remboursé'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    provider = models.CharField(max_length=20, choices=PROVIDER_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=200, blank=True)
    reference = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Paiement'

    def __str__(self):
        return f'Paiement {self.provider} — {self.order.order_number}'
