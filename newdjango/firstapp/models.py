# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # The name of the product
    description = models.TextField()  # A detailed description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # The price of the product
    stock = models.IntegerField()  # The number of items available in stock
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the product was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the product was last updated
    is_active = models.BooleanField(default=True)  # Whether the product is active or not
    sku = models.CharField(max_length=100, unique=True)  # Stock Keeping Unit identifier
    category = models.CharField(max_length=100)  # The category of the product
    manufacturer = models.CharField(max_length=100)  # The manufacturer of the product

    def __str__(self):
        return self.name

