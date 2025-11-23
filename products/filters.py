# filters.py
from products.models import Product
from django.db.models import Q

def filter_products(filters: dict):
    queryset = Product.objects.all()

    # Category filtering
    category = filters.get("category")
    if category:
        queryset = queryset.filter(category__icontains=category)

    # Color filtering
    color = filters.get("color")
    if color:
        queryset = queryset.filter(color__icontains=color)

    # Price filtering
    min_price = filters.get("min_price")
    max_price = filters.get("max_price")

    if min_price is not None:
        queryset = queryset.filter(price__gte=min_price)

    if max_price is not None:
        queryset = queryset.filter(price__lte=max_price)

    # Keyword search
    keywords = filters.get("keywords", [])
    for kw in keywords:
        queryset = queryset.filter(
            Q(title__icontains=kw) |
            Q(description__icontains=kw)
        )

    return queryset
