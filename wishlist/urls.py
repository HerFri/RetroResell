from django.urls import path
#from .models import Wishlist
from .views import WishlistView, RemovefromWishlist, AddToWishlist
from . import views

urlpatterns = [
    #path('', views.view_wishlist, name='view_wishlist'),
    path('wishlist/', WishlistView.as_view(), name='view_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', RemovefromWishlist.as_view(), name='remove_from_wishlist'),
    path('add_to_wishlist/<int:product_id>/', AddToWishlist.as_view(), name='add_to_wishlist'),
]
