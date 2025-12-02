from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomerProfile
from .serializers import customer_profile_serializer


class CustomerProfileView(APIView):
    def get(self, request):
        user = request.user
        try:
            profile = CustomerProfile.objects.get(user=user)
            serializer = customer_profile_serializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomerProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)