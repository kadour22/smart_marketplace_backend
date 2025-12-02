from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from products.models import Product, Wishlist
from products.serializers import product_serializer, product_list_serializer , wishlist_serializer
from rest_framework import status

# def products list service
def list_products_service():
    products = Product.objects.all()
    serializer = product_list_serializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# def product detail service
def product_detail_service(product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer = product_serializer(product)
    return Response({"result": serializer.data}, status=status.HTTP_200_OK)

# def create product service
def create_product_service(product_data):
    serializer = product_serializer(data=product_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# delete product service
def delete_product_service(product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# add to wishlist service
def add_to_wishlist_service(user, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    wishlist.products.add(product)
    serializer = wishlist_serializer(wishlist)
    return Response(serializer.data, status=status.HTTP_200_OK)
        