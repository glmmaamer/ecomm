from django.shortcuts import render
from . models import *
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    product = Product.objects.all()
    return render(request, 'home.html',{'product':product})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    return render(request, 'logout.html')