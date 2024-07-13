from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import ShippingForm, PaymentForm
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product


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
                                                    'shipping_form':shipping_form,
                                                    })
    else:
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'payment/checkout.html',{'cart_products':products,
                                                        'cart_quantity':quantity,
                                                        'cart_total':totales,
                                                        'shipping_form':shipping_form
                                                        })

def billin_info(request):
    if request.POST:
        cart = Cart(request)
        products = cart.get_prods
        quantity = cart.get_quantites
        totales = cart.cart_total()
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping
        if request.user.is_authenticated:
            billing_form = PaymentForm()
            return render(request, 'payment/billing_info.html',{'cart_products':products,
                                                                'cart_quantity':quantity,
                                                                'cart_total':totales,
                                                                'shipping_info':request.POST,
                                                                'billing_form':billing_form
                                                                })
        else:
            billing_form = PaymentForm()
            return render(request, 'payment/billing_info.html',{'cart_products':products,
                                                                'cart_quantity':quantity,
                                                                'cart_total':totales,
                                                                'shipping_info':request.POST,
                                                                'billing_form':billing_form
                                                                })

        shipping_form = request.POST
        return render(request, 'payment/billing_info.html',{'cart_products':products,
                                                            'cart_quantity':quantity,
                                                            'cart_total':totales,
                                                            'shipping_form':shipping_form,
                                                            })

            
    else:
        messages.success(request,('تم إرسال الطلب'))
        return redirect('home')
    
def process_order(request):

    if request.POST:
        cart = Cart(request)
        products = cart.get_prods
        quantity = cart.get_quantites
        totals = cart.cart_total()
        payment_form = PaymentForm(request.POST or None)
        my_shipping = request.session.get('my_shipping')
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']

        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_country']}"
        amount_paid = totals
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            order_id = create_order.pk
            for product in products():
                product_id = product.id
                if product.is_sale:
                    price = product.is_sale
                else:
                    price = product.price

                for key, value in quantity().items():
                    if int(key) == product.id:
                        create_order_item = OrderItem(order_id=order_id ,product_id=product_id ,user=user, quantity=value, price=price)
                        create_order_item.save()
            for key in list(request.session.keys()):
                if key == "session_key":
                    del request.session[key]

            messages.success(request,'يتم  معالجة الطلب')
            return redirect('home')
        else:
            create_order = Order( full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            order_id = create_order.pk
            for product in products():
                product_id = product.id
                if product.is_sale:
                    price = product.is_sale
                else:
                    price = product.price

                for key, value in quantity().items():
                    if int(key) == product.id:
                        create_order_item = OrderItem(order_id=order_id ,product_id=product_id , quantity=value, price=price)
                        create_order_item.save()
            for key in list(request.session.keys()):
                if key == "session_key":
                    del request.session[key]
                        
            messages.success(request,'يتم  معالجة الطلب')
            return redirect('home')

        

    else:
        messages.success(request,'لم يتم إرسال الطلب')
        return redirect('home')
    