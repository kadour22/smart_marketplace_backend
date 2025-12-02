from rest_framework import serializers
from .models import CustomerProfile


class customer_profile_serializer(serializers.ModelSerializer) :
    listed_products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta :
        model = CustomerProfile
        fields = "__all__"
        read_only_fields = ['listed_products']