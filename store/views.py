from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm



# Create your views here.
def category_all(request):
    all_category = Category.objects.all()
    return render(request, 'category_all.html',{"all_category":all_category})


def category(request,foo):
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html',{'products':products,'category':category })
    except:
        messages.success(request,('category try again'))
        return redirect('home')

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html',{'product':product})

def home(request):
    product = Product.objects.all()
    return render(request, 'home.html',{'product':product})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == "POST":
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

def Register_User(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,('You have regester Successfully  '))
            return redirect('home')
        else:
            messages.success(request, ('problem with regester pls try again...'))
            return redirect('home')
    else:
        return render(request, 'signup.html',{'form':form}) 