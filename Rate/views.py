from rest_framework.views import APIView
from .service.rate_service import rate_seller_service

class rate_seller_view(APIView) :
    def post(self,request) :
        return rate_seller_service(
            rate_data=request.data,
            rate_by=request.user
        )