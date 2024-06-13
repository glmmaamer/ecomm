from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.summary, name='summary'),
    path('add/',views.cart_add, name='cart_add'),
    path('update/',views.update_cart, name='update_cart'),
    path('delete/',views.delete, name='delete'),
]