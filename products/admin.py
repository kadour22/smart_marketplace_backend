from django.contrib import admin
from .models import Product,Wishlist, HistorySearch

admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(HistorySearch)