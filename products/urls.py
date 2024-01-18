from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('comment/edit/<int:comment_id>/', views.edit_comment,
         name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
]
