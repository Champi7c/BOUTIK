from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Size, Color, ProductReview, Wishlist, Banner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'order', 'is_active', 'product_count')
    list_filter = ('is_active', 'parent')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Produits'


class ProductImageInline(admin.TabularInline):
    model = Product
    extra = 0
    fields = ('image',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_image', 'name', 'category', 'price_display',
        'stock_display', 'is_new', 'is_featured', 'is_active', 'sales_count'
    )
    list_filter = ('category', 'is_new', 'is_featured', 'is_active')
    list_editable = ('is_new', 'is_featured', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('sizes', 'colors')
    readonly_fields = ('views_count', 'sales_count', 'created_at', 'updated_at', 'product_image_preview')
    ordering = ('-created_at',)

    fieldsets = (
        ('Informations de base', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Prix & Stock', {
            'fields': ('price', 'discount_price', 'stock')
        }),
        ('Options', {
            'fields': ('sizes', 'colors')
        }),
        ('Images', {
            'fields': ('image', 'image2', 'image3', 'product_image_preview')
        }),
        ('Statuts', {
            'fields': ('is_featured', 'is_new', 'is_active')
        }),
        ('Statistiques', {
            'fields': ('views_count', 'sales_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def product_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:2px">',
                obj.image.url
            )
        return '—'
    product_image.short_description = 'Photo'

    def product_image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:200px;height:auto;object-fit:cover">',
                obj.image.url
            )
        return '—'
    product_image_preview.short_description = 'Aperçu'

    def price_display(self, obj):
        if obj.discount_price:
            return format_html(
                '<s style="color:#999">{}</s> <strong style="color:#28a745">{}</strong> FCFA',
                f'{int(obj.price):,}', f'{int(obj.discount_price):,}'
            )
        return format_html('<strong>{}</strong> FCFA', f'{int(obj.price):,}')
    price_display.short_description = 'Prix'

    def stock_display(self, obj):
        color = '#28a745' if obj.stock > 5 else ('#FFA500' if obj.stock > 0 else '#dc3545')
        return format_html('<span style="color:{}"><strong>{}</strong></span>', color, obj.stock)
    stock_display.short_description = 'Stock'


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_preview', 'hex_code')

    def color_preview(self, obj):
        return format_html(
            '<div style="width:30px;height:30px;border-radius:50%;background:{};border:1px solid #ddd"></div>',
            obj.hex_code
        )
    color_preview.short_description = 'Couleur'


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    readonly_fields = ('created_at',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
