from django import forms
from django.contrib.auth.models import User

from apps.store.models import Product, Category, Banner, Size, Color
from apps.orders.models import Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'category', 'description', 'price', 'discount_price',
            'sizes', 'colors', 'stock', 'image', 'image2', 'image3',
            'is_featured', 'is_new', 'is_active',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'dash-input'}),
            'name': forms.TextInput(attrs={'class': 'dash-input'}),
            'category': forms.Select(attrs={'class': 'dash-input'}),
            'price': forms.NumberInput(attrs={'class': 'dash-input', 'min': 0}),
            'discount_price': forms.NumberInput(attrs={'class': 'dash-input', 'min': 0}),
            'stock': forms.NumberInput(attrs={'class': 'dash-input', 'min': 0}),
            'image': forms.FileInput(attrs={'class': 'dash-input'}),
            'image2': forms.FileInput(attrs={'class': 'dash-input'}),
            'image3': forms.FileInput(attrs={'class': 'dash-input'}),
            'sizes': forms.CheckboxSelectMultiple,
            'colors': forms.CheckboxSelectMultiple,
        }
        labels = {
            'name': 'Nom du produit',
            'category': 'Catégorie',
            'description': 'Description',
            'price': 'Prix (FCFA)',
            'discount_price': 'Prix promo (FCFA)',
            'stock': 'Stock',
            'image': 'Image principale',
            'image2': 'Image 2',
            'image3': 'Image 3',
            'is_featured': 'En vedette',
            'is_new': 'Nouveauté',
            'is_active': 'Actif (visible sur le site)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(is_active=True)
        self.fields['discount_price'].required = False
        if self.instance.pk:
            self.fields['image'].required = False
            self.fields['image'].help_text = 'Laisser vide pour conserver l\'image actuelle.'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent', 'description', 'image', 'order', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'dash-input'}),
            'parent': forms.Select(attrs={'class': 'dash-input'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'dash-input'}),
            'image': forms.FileInput(attrs={'class': 'dash-input'}),
            'order': forms.NumberInput(attrs={'class': 'dash-input', 'min': 0}),
        }
        labels = {
            'name': 'Nom',
            'parent': 'Catégorie parente',
            'description': 'Description',
            'image': 'Image',
            'order': 'Ordre d\'affichage',
            'is_active': 'Active',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Category.objects.filter(parent=None)
        self.fields['parent'].required = False
        if self.instance.pk:
            self.fields['image'].required = False


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['title', 'subtitle', 'image', 'link', 'button_text', 'is_active', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'dash-input'}),
            'subtitle': forms.TextInput(attrs={'class': 'dash-input'}),
            'link': forms.TextInput(attrs={'class': 'dash-input'}),
            'button_text': forms.TextInput(attrs={'class': 'dash-input'}),
            'image': forms.FileInput(attrs={'class': 'dash-input'}),
            'order': forms.NumberInput(attrs={'class': 'dash-input', 'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['image'].required = False


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'payment_status', 'notes']
        widgets = {
            'status': forms.Select(attrs={'class': 'dash-input'}),
            'payment_status': forms.Select(attrs={'class': 'dash-input'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'dash-input'}),
        }
        labels = {
            'status': 'Statut commande',
            'payment_status': 'Statut paiement',
            'notes': 'Notes internes',
        }


class StockAdjustForm(forms.Form):
    stock = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'dash-input stock-input'}))


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['name', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'dash-input'}),
            'order': forms.NumberInput(attrs={'class': 'dash-input', 'min': 0}),
        }


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'hex_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'dash-input'}),
            'hex_code': forms.TextInput(attrs={'class': 'dash-input', 'type': 'color'}),
        }


class CustomerStaffForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_active', 'is_staff']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'dash-input'}),
            'last_name': forms.TextInput(attrs={'class': 'dash-input'}),
            'email': forms.EmailInput(attrs={'class': 'dash-input'}),
        }
        labels = {
            'is_active': 'Compte actif',
            'is_staff': 'Accès dashboard admin',
        }
