from rest_framework import serializers
from .models import Product, Wishlist

class product_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        fields = "__all__"
        read_only_fields = ['embedding', 'seller']

class product_list_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        fields = ['id', 'product_name', 'price', 'image']

class wishlist_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Wishlist
        fields = ["user", "products"]
        read_only_fields = ['user']