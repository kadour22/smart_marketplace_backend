from django.db import models
from pgvector.django import VectorField
from django.contrib.auth.models import User

class Product(models.Model) :
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="products_images/")
    embedding = VectorField(null=True , blank=True) 

    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name