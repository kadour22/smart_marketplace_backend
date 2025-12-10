from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import RateSeller

class RateSellerSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model  = RateSeller
        fields = ["seller", "rate_by", "rate_value", "created_at"]
        read_only_fields = ["rate_by"]
    
    def validate(self, data):
        if "rate_value" not in data:
            raise serializers.ValidationError(
                {"rate_value": "You must include rate_value in your request."}
            )
        value = data.get("rate_value")
        if not value:
            raise ValidationError("rate value is required . .")
        if not (0 <= value <= 10):
            raise ValidationError("rate must be between 0 and 10")
        return data
