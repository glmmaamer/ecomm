from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantites = cart.get_quantites
    return render(request, 'cart.html',{'cart_products':cart_products,
                                        'quantites': quantites
                                        })

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()

        #response = JsonResponse({'Product Name: ':product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response
    

def update(request):
    pass

def delete(request):
    pass