from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.summary, name='summary'),
    path('add/',views.add, name='add'),
    path('update/',views.update, name='update'),
    path('delete/',views.delete, name='delete'),
]