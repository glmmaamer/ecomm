from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def summary(request):
    return render(request, 'cart.html')

def cart_add(request):
    pass

def update(request):
    pass

def delete(request):
    pass