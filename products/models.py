from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Product(models.Model) :
    product_name = models.CharField(max_length=255)
    category     = models.CharField(max_length=100 , null=True, blank=True)
    color        = models.CharField(max_length=50, null=True, blank=True)
    price        = models.DecimalField(max_digits=6,decimal_places=2)
    description  = models.TextField(null=True, blank=True)
    image        = models.ImageField(upload_to="products_images/")
    embedding    = ArrayField(base_field=models.FloatField(), size=1536, null=True, blank=True)

    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='wishlisted_by')

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

