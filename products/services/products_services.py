from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from products.models import Product
from products.serializers import product_serializer
from rest_framework import status


# def products list service
def list_products_service():
    products = Product.objects.all()
    serializer = product_serializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# def product detail service
def product_detail_service(product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer = product_serializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
# def create product service
def create_product_service(product_data):
    serializer = product_serializer(data=product_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)