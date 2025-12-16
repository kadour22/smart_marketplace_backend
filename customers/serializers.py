from rest_framework import serializers
from .models import CustomerProfile
from django.contrib.auth.models import User
from products.models import Wishlist , Product

class customer_profile_serializer(serializers.ModelSerializer) :
    listed_products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta :
        model = CustomerProfile
        fields = "__all__"
        read_only_fields = ['listed_products']

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name','image']

class wishlist_serializer(serializers.ModelSerializer):
    products = product_serializer(many=True, read_only=True)
    class Meta:
        model = Wishlist
        fields = ['id', 'products']

class user_serializer(serializers.ModelSerializer) :
    wishlist = wishlist_serializer(many=True, read_only=True)
    class Meta :
        model = User
        fields = ['id', 'username', 'wishlist']

class create_customer_serializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = [
            "username","email","password"
        ] 
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user