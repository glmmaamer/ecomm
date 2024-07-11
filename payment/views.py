from django.shortcuts import render
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress

# Create your views here.

def payment_success(request):
    
    return render(request, "payment/payment.html")

def checkout(request):
    cart = Cart(request)
    products = cart.get_prods
    quantity = cart.get_quantites
    totales = cart.cart_total()
    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request,'payment/checkout.html',{'cart_products':products,
                                                    'cart_quantity':quantity,
                                                    'cart_total':totales,
                                                    'shipping_form':shipping_form
                                                    })
    else:
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'payment/checkout.html',{'cart_products':products,
                                                        'cart_quantity':quantity,
                                                        'cart_total':totales,
                                                        'shipping_form':shipping_form
                                                        })
