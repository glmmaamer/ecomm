from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantites = cart.get_quantites
    total = cart.cart_total()
    
    return render(request, 'cart.html',{'cart_products':cart_products,
                                        'quantites': quantites,
                                        'totales':total})

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
        messages.success(request,( 'تمت إضافة منتج إلى السلة'))
        return response
    


def update_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request,('تم تحديث الصفحة'))
        return response
        #return redirect('summary')

def delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delet(product=product_id)

        respons = JsonResponse({'porduct':product_id})
        messages.success(request,('تم حذف المنتج من سلة الشراء'))
        return respons