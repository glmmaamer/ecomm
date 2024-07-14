from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_success, name='payment_success'),
    path('checkout/', views.checkout, name='checkout'),
    path('billing_info/',views.billin_info, name='billing_info'),
    path('process_order/',views.process_order, name='process_order'),
    path('shipped/',views.shipped, name='shipped'),
    path('not_shipped/',views.not_shipped, name='not_shipped'),

]