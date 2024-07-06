from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.cart_add, name='cart_add'),
    path('update/',views.update_cart, name='update_cart'),
    path('delete/',views.delete, name='delete_cart'),
    path('cart/',views.summary, name='summary'),

]