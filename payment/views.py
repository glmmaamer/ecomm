from django.shortcuts import render
from cart.cart import Cart

# Create your views here.

def payment_success(request):
    
    return render(request, "payment/payment.html")

def checkout(request):
    cart = Cart(request)
    products = cart.get_prods
    quantity = cart.get_quantites
    totales = cart.cart_total()
    return render(request, 'payment/checkout.html',{'cart_products':products,
                                                    'cart_quantity':quantity,
                                                    'cart_total':totales
                                                    })
