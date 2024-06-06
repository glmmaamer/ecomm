from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from .forms import CreateUser

# Create your views here.


def home(request):
    product = Product.objects.all()
    return render(request, 'home.html',{'product':product})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("login for your user admin "))
            return redirect('home')
        else:
            messages.success(request,("error plz try egain"))
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("you have been logged out"))
    redirect('home')

def Register(request):
    form = CreateUser()
    return render(request, 'signup.html',{
        'form':form
    })