from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    PARENT_CHOICES = [
        ('chaussures', 'Chaussures'),
        ('homme', 'Vêtements Homme'),
        ('femme', 'Vêtements Femme'),
        ('accessoires', 'Accessoires'),
        ('nouveautes', 'Nouveautés'),
        ('soldes', 'Soldes'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='children'
    )
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('store:category', kwargs={'slug': self.slug})


class Size(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Taille'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, default='#000000')

    class Meta:
        verbose_name = 'Couleur'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nom')
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products', verbose_name='Catégorie'
    )
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(
        max_digits=10, decimal_places=0,
        verbose_name='Prix (FCFA)'
    )
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=0,
        null=True, blank=True, verbose_name='Prix promo (FCFA)'
    )
    sizes = models.ManyToManyField(Size, blank=True, verbose_name='Tailles')
    colors = models.ManyToManyField(Color, blank=True, verbose_name='Couleurs')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    image = models.ImageField(
        upload_to='products/', verbose_name='Image principale'
    )
    image2 = models.ImageField(
        upload_to='products/', null=True, blank=True, verbose_name='Image 2'
    )
    image3 = models.ImageField(
        upload_to='products/', null=True, blank=True, verbose_name='Image 3'
    )
    is_featured = models.BooleanField(default=False, verbose_name='En vedette')
    is_new = models.BooleanField(default=True, verbose_name='Nouveau')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    views_count = models.IntegerField(default=0)
    sales_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'slug': self.slug})

    @property
    def current_price(self):
        return self.discount_price if self.discount_price else self.price

    @property
    def discount_percent(self):
        if self.discount_price and self.price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return 0

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return round(sum(r.rating for r in reviews) / len(reviews), 1)
        return 0

    @property
    def is_in_stock(self):
        return self.stock > 0


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Avis'
        verbose_name_plural = 'Avis'
        unique_together = ('product', 'user')

    def __str__(self):
        return f'{self.user.username} — {self.product.name}'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Favori'
        verbose_name_plural = 'Favoris'
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user.username} — {self.product.name}'


class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='banners/')
    link = models.CharField(max_length=200, blank=True)
    button_text = models.CharField(max_length=50, default='Découvrir')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Bannière'
        ordering = ['order']

    def __str__(self):
        return self.title
