from rest_framework import status
from rest_framework.response import Response

from Rate.models import RateSeller
from Rate.serializers import RateSellerSerializer

def rate_seller_service(rate_data,rate_by) :
    serializer = RateSellerSerializer(data=rate_data)
    if serializer.is_valid() :

        seller   = serializer.validated_data["seller"]
        existing = RateSeller.objects.filter(
                rate_by=rate_by,
                seller=seller
            ).first()
        if existing :
                return Response({
                    "message" : "you can rate seller only one time"
                })
        serializer.save(rate_by=rate_by)
        return Response(serializer.data , status=200)
    
    return Response(serializer.errors , status=400)

            
