from django.conf import settings
from apps.store.models import Product


class Cart:
    """Panier géré en session."""

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, size=None, color=None, override_quantity=False):
        product_id = str(product.id)
        key = f"{product_id}_{size or ''}_{color or ''}"
        if key not in self.cart:
            self.cart[key] = {
                'product_id': product_id,
                'quantity': 0,
                'price': str(product.current_price),
                'size': size,
                'color': color,
                'name': product.name,
                'image': product.image.url if product.image else '',
                'slug': product.slug,
            }
        if override_quantity:
            self.cart[key]['quantity'] = quantity
        else:
            self.cart[key]['quantity'] += quantity
        self.save()

    def remove(self, key):
        if key in self.cart:
            del self.cart[key]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __iter__(self):
        product_ids = [v['product_id'] for v in self.cart.values()]
        products = Product.objects.filter(id__in=product_ids)
        products_map = {str(p.id): p for p in products}

        for key, item in self.cart.items():
            item = item.copy()
            item['key'] = key
            product = products_map.get(item['product_id'])
            if product:
                item['product'] = product
                item['total_price'] = int(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def is_empty(self):
        return len(self.cart) == 0
