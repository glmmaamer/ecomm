from django.shortcuts import render

# Create your views here.

def summary(request):
    return render(request, 'cart.html')

def add(request):
    pass

def update(request):
    pass

def delete(request):
    pass