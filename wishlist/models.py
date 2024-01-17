from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Wishlist(models.Model):
    """Model for Wishlist"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)