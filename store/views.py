from django.shortcuts import render, redirect
from .models import Profile, Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordFrom, UserInfoForm
from django.db.models import Q

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
            return redirect('update_info')
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
            messages.success(request, ("تم تسجيل دخول "))
            return redirect('home')
        else:
            messages.success(request,("هناك خطأ في تسجيل الدخول يرجى إعادة المحاولة"))
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def update_info(request):
    if request.user.is_authenticated:
        current_info = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_info)
        if form.is_valid():
            form.save()
            messages.success(request, ('تمت إضافة و تعديل جميع بياناتك '))
            return redirect('home')
        return render(request, 'update_info.html',{'form':form})
    else:
        messages.success(request, ('هناك خطأفي أضافة أو تعديل بيانات توصيل عند الشراء يرجى إعادة المحاولة'))
        return redirect('home')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        update_form = UpdateUserForm(request.POST or None, instance=current_user)
        if update_form.is_valid():
            update_form.save()
            login(request, current_user)
            messages.success(request,('تم تحديث ملفك الشخصي'))
            return redirect('home')
        return render(request, 'update_user.html', {'update_form':update_form})
    else:
        messages.success(request, ('لم يتم تحديث ملفك الشخصي هناك خطأ'))
        return redirect('home')

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

