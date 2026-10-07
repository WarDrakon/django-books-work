from django import template
from books.models import Book

register = template.Library()

@register.filter(name='uah')
def uah_currency(value):
    if value is None:
        return ""
    return f"{value} грн"

@register.simple_tag
def product_count():
    return Book.objects.count()