from django.shortcuts import render, redirect
from .models import Profile, Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordFrom, UserInfoForm

from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.db.models import Q
import json
from cart.cart import Cart
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

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.success(request, ('منتج غير موجود'))
            return render(request,'search.html')
        else:
            return render(request, 'search.html',{'searched':searched})

    else:
        return render(request, 'search.html')

def home(request):
    product = Product.objects.all()
    return render(request, 'home.html',{'product':product})

def about(request):
    return render(request, 'about.html')

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
            messages.success(request,('تم إنشاء حساب بنجاح  '))
            return redirect('update_user')
        else:
            messages.success(request, ('لم يتم إنشاء حساب يرجى إعادة المحاولة'))
            return redirect('home')
    else:
        return render(request, 'signup.html',{'form':form}) 
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.cart_old
            if saved_cart:
                convarted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key,value in convarted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, ("تم تسجيل دخول "))
            return redirect('home')
        else:
            messages.success(request,("هناك خطأ في تسجيل الدخول يرجى إعادة المحاولة"))
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        update_form = UpdateUserForm(request.POST or None, instance=current_user)
        if update_form.is_valid():
            update_form.save()
            login(request, current_user)
            messages.success(request, 'تم تعديل بيانات ملفك الشخصي')
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id )
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if shipping_form.is_valid():
            shipping_form.save()
            messages.success(request,('تم تحديث بيانات الشحن'))
            return redirect('home')
        return render(request,'update_user.html',{'update_form':update_form, 'shipping_form':shipping_form})
    else:
        messages.success(request, ('لم يتم تحديث ملفك الشخصي هناك خطأ'))
        return redirect('home')
    #update info


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            pass_form = UpdatePasswordFrom(current_user,request.POST)
            if pass_form.is_valid():
                pass_form.save()
                messages.success(request, ('تم تحديث كلمة السر'))
                #login(request,current_user)
                return redirect('login')
            else:
                for error in list(pass_form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            pass_form= UpdatePasswordFrom(current_user)
            return render(request, 'update_password.html',{'pass_form':pass_form})
    else:
        messages.success(request, ('لم يتم تحديث كلمة السر'))
        return redirect('home')


def logout_user(request):
    logout(request)
    messages.success(request,("تم تسجيل الخروج "))
    return redirect('login')

def deshpoard(request):
    return render(request, 'payment/dashpord.html')