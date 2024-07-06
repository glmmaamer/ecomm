from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('signup/',views.Register_User, name='signup'),
    path('update_password',views.update_password, name='update_password'),
    path('update_user/',views.update_user, name='update_user'),
    path('product/<int:pk>/',views.product, name='product'),
    path('category/<str:foo>',views.category, name='category'),
    path('catgery_all/',views.category_all, name='category_all')
]