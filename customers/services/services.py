
from rest_framework.response import Response
from rest_framework import status

from customers.models import CustomerProfile
from customers.serializers import (
    customer_profile_serializer,
    user_serializer,
    create_customer_serializer
)

def customer_profile(user) :
    try:
        profile = CustomerProfile.objects.get(user=user)
        serializer = customer_profile_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except CustomerProfile.DoesNotExist:
        return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

def customer_wishlist(user) :
    try:
        user = user
        serializer = user_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
            print(e)
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)