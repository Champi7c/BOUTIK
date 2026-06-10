from django.db import models
from django.contrib.auth.models import User
from apps.store.models import Product, Size, Color


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.quantity}x {self.product.name}'

    @property
    def subtotal(self):
        return self.unit_price * self.quantity


class Order(models.Model):
    STATUS = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('preparing', 'En préparation'),
        ('shipped', 'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]
    DELIVERY_CHOICES = [
        ('ouest_foire', 'Retrait Ouest Foire'),
        ('guediawaye', 'Retrait Guediawaye'),
        ('colobane', 'Retrait Colobane'),
        ('livraison', 'Livraison à domicile'),
    ]
    PAYMENT_CHOICES = [
        ('wave', 'Wave'),
        ('orange_money', 'Orange Money'),
        ('stripe', 'Carte bancaire (Visa / Mastercard)'),
        ('cash', 'Paiement à la livraison'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='orders', verbose_name='Client'
    )
    items = models.ManyToManyField(OrderItem, verbose_name='Articles')
    total = models.DecimalField(
        max_digits=10, decimal_places=0, verbose_name='Total (FCFA)'
    )
    status = models.CharField(
        max_length=20, choices=STATUS,
        default='pending', verbose_name='Statut'
    )
    delivery_type = models.CharField(
        max_length=20, choices=DELIVERY_CHOICES,
        default='livraison', verbose_name='Livraison'
    )
    delivery_address = models.TextField(
        blank=True, verbose_name='Adresse de livraison'
    )
    delivery_fee = models.DecimalField(
        max_digits=6, decimal_places=0, default=0,
        verbose_name='Frais de livraison'
    )
    phone = models.CharField(max_length=20, verbose_name='Téléphone')
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_CHOICES,
        default='cash', verbose_name='Paiement'
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[('pending', 'En attente'), ('paid', 'Payé'), ('failed', 'Échoué')],
        default='pending'
    )
    order_number = models.CharField(max_length=20, unique=True, blank=True)
    notes = models.TextField(blank=True, verbose_name='Notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'
        ordering = ['-created_at']

    def __str__(self):
        return f'Commande #{self.order_number} — {self.user.username}'

    def save(self, *args, **kwargs):
        if not self.order_number:
            import random
            import string
            self.order_number = 'TS' + ''.join(
                random.choices(string.digits, k=6)
            )
        super().save(*args, **kwargs)

    @property
    def grand_total(self):
        return self.total + self.delivery_fee

    def get_status_color(self):
        colors = {
            'pending': 'warning',
            'confirmed': 'info',
            'preparing': 'primary',
            'shipped': 'info',
            'delivered': 'success',
            'cancelled': 'danger',
        }
        return colors.get(self.status, 'secondary')


class Cart(models.Model):
    """Panier persistant pour les utilisateurs connectés."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Panier'

    def __str__(self):
        return f'Panier de {self.user.username}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Article panier'

    def __str__(self):
        return f'{self.quantity}x {self.product.name}'

    @property
    def subtotal(self):
        return self.product.current_price * self.quantity
