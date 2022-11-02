from django.shortcuts import render

# Create your views here.
def Customer_home(request):
    return render(request,'Customer_templates/home.html')
def Customer_cart(request):
    return render(request,'Customer_templates/cart.html')
    