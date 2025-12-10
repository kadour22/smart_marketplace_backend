from django.db import models
from django.contrib.auth.models import User

class RateSeller(models.Model) :
    seller  = models.ForeignKey(User, on_delete=models.CASCADE , related_name='rate')
    rate_by = models.ForeignKey(User , on_delete=models.CASCADE, related_name='my_rates') 
    rate_value = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.seller.username}"