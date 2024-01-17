from django.contrib import admin
from .models import Wishlist

# Register your models here.
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'added_on',
    )

admin.site.register(Wishlist, WishlistAdmin)