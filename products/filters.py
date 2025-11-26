# filters.py
from products.models import Product
from django.db.models import Q, F
from decimal import Decimal

def filter_products(filters: dict):
    queryset = Product.objects.all()

    category = filters.get("category")
    if category:
        queryset = queryset.filter(category__icontains=category)

    color = filters.get("color")
    if color:
        queryset = queryset.filter(color__icontains=color)

    min_price = filters.get("min_price")
    max_price = filters.get("max_price")

    if min_price is not None:
        queryset = queryset.filter(price__gte=Decimal(min_price))
    if max_price is not None:
        queryset = queryset.filter(price__lte=Decimal(max_price))

    keywords = filters.get("keywords", [])
    for kw in keywords:
        queryset = queryset.filter(
            Q(product_name__icontains=kw) |
            Q(description__icontains=kw)
        )

    return queryset
