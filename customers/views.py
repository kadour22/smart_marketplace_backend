from rest_framework.views import APIView
from .services.services import (
    customer_profile,
    customer_wishlist,
    create_customer
)

class CustomerProfileView(APIView):
    def get(self, request):
        return customer_profile(user=request.user)

class customer_wishlist_view(APIView):
    def get(self, request):
        return customer_wishlist(user=request.user)

class create_customer_view(APIView) :
    def post(self,request) :
        return create_customer(data=request.data)