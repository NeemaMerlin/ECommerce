from django.urls import path
from . import views

urlpatterns=[
    path('home', views.Customer_home),
    path('cart',views.Customer_cart),
]
