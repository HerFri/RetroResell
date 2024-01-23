from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    """
    A class allowing the admin to manage inquiries on the admin panel
    """
    list_display = ('user', 'subject', 'image', 'user_message', 'created_on', 'order_number')

