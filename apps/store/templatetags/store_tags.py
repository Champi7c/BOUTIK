from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def split(value, sep=','):
    """Split a string by separator."""
    return value.split(sep)


@register.filter
def intcomma(value):
    """Format number with spaces as thousands separator."""
    try:
        return f'{int(value):,}'.replace(',', ' ')
    except (ValueError, TypeError):
        return value


@register.filter
def stars_range(value):
    """Return range for star rating."""
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return range(0)


@register.simple_tag
def cart_item_total(price, quantity):
    try:
        return int(float(price)) * int(quantity)
    except (ValueError, TypeError):
        return 0
