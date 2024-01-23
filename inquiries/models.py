from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Inquiry(models.Model):
    """A model for customer inquiries"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=200)
    order_number = models.CharField(max_length=100, null=True, blank=True)
    user_message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    admin_reply = models.TextField(null=True, blank=True)
    user_reply = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'inquiries'

    def __str__(self):
        return self.name

        
