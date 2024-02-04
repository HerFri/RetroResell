from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from .models import Wishlist
from django.contrib import messages
# Create your views here.

class WishlistView(LoginRequiredMixin, View):
    """A view to return the wishlist page"""
    def get(self, request):
        user = request.user
        wishlist_items = Wishlist.objects.filter(user=user)
        context = {
            "wishlist_items": wishlist_items,
        }

        return render(request, 'wishlist.html', context)

class AddToWishlist(LoginRequiredMixin, View):
    """A view to add products to wishlist"""
    def post(self, request, product_id):
        
        user = request.user
        product = get_object_or_404(Product, id=product_id)
        wishlist_item = Wishlist.objects.filter(user=user, product=product)
        wishlist_item_count = Wishlist.objects.count()

        if wishlist_item.exists():
            messages.info(request, f'{product.name} is already in your wishlist!')
        else:
            if wishlist_item_count >= 5:
                messages.info(request, "You have reached the maximum number of items in your wishlist!")
            else:
                wishlist_item = Wishlist.objects.create(user=user, product=product)
                messages.info(request, f'{product.name} was added to your wishlist!')
        print(wishlist_item_count)
        return redirect(reverse('product_detail', kwargs={'product_id': product_id}))

class RemovefromWishlist(LoginRequiredMixin, View):
    """A view to remove products from wishlist"""
    def post(self, request, product_id):
        
        user = request.user
        product = get_object_or_404(Product, id=product_id)
        wishlist_item = Wishlist.objects.filter(product_id=product)

        if wishlist_item.exists():
            wishlist_item.delete()
            messages.info(request, f'{product.name} was removed from your wishlist!')
        else:
            messages.info(request, f'{product.name} is not in your wishlist!')
            
        return redirect(reverse('view_wishlist'))