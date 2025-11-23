from rest_framework.response import Response
from products.models import Product
from products.serializers import product_serializer
from rest_framework import status


# def products list service
def list_products_service():
    products = Product.objects.all()
    serializer = product_serializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)