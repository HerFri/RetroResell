from django.urls import path
from . import views

urlpatterns = [
    path('inquiries/', views.user_inquiry, name='inquiries'),
    path('inquiry/<int:inquiry_id>/', views.view_inquiry, name='inquiry'),
    path('delete_inquiry/<int:inquiry_id>/',
        views.delete_inquiry, name='delete_inquiry'
        ),
]