from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='customer_profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    first_name   = models.CharField(max_length=30, blank=True, null=True)
    last_name    = models.CharField(max_length=30, blank=True, null=True)
    address      = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"