from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='customer_profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    first_name   = models.CharField(max_length=30, blank=True, null=True)
    last_name    = models.CharField(max_length=30, blank=True, null=True)
    address      = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


"""
   seller contacts (seller , sender , product , email , message,phone_number , )

"""
class SellerContact(models.Model):
    seller      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_contacts')
    sender      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_contacts')
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_contacts')
    email       = models.EmailField()
    message     = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.sender.username} to {self.seller.username} about {self.product.name}"