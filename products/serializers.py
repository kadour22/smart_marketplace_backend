from rest_framework import serializers
from .models import Product, Wishlist , HistorySearch

class product_serializer(serializers.ModelSerializer) :
    
    class Meta :
        model = Product
        fields = "__all__"
        read_only_fields = ['embedding', 'seller']

class product_list_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        fields = ['id', 'product_name', 'price', 'image','description']

class wishlist_serializer(serializers.ModelSerializer) :
    
    class Meta :
        model = Wishlist
        fields = ["user", "products"]
        read_only_fields = ['user']

class historySearchSerializer(serializers.ModelSerializer) :
    class Meta :
        model = HistorySearch
        fields= "__all__"