from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomerProfile
from .serializers import customer_profile_serializer, user_serializer


class CustomerProfileView(APIView):
    def get(self, request):
        user = request.user
        try:
            profile = CustomerProfile.objects.get(user=user)
            serializer = customer_profile_serializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomerProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

class customer_wishlist_view(APIView):
    def get(self, request):
        try:
            user = request.user
            serializer = user_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)