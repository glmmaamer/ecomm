from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_success, name='payment_success'),
    path('checkout/', views.checkout, name='checkout')
]