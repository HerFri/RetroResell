from django.db import models
from .genres import GENRES  
from .platforms import PLATFORMS
from .stars import STARS


class Category(models.Model):
    """Model for Product Category"""

    class Meta:	
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    """Model for Product"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    genre = models.CharField(max_length=100, choices=GENRES, null=True, blank=True)
    platform = models.CharField(max_length=100, choices=PLATFORMS, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(choices=STARS, max_digits=2, decimal_places=1, default=0)
    #rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
