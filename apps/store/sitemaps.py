from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Category


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Product.objects.filter(is_active=True).order_by('-updated_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class CategorySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return Category.objects.filter(is_active=True).order_by('order')

    def location(self, obj):
        return obj.get_absolute_url()


class StaticSitemap(Sitemap):
    changefreq = 'monthly'
    protocol = 'https'

    pages = [
        ('store:home',        1.0),
        ('store:product_list', 0.8),
        ('store:about',        0.5),
        ('store:contact',      0.5),
    ]

    def items(self):
        return self.pages

    def priority(self, item):
        return item[1]

    def location(self, item):
        return reverse(item[0])
