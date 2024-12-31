from django.shortcuts import render,HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    products= Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    context= {'no_of_slides':nSlides, 'range': range(nSlides), 'product': products}
    return render(request, 'shop/index.html',context)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def prodview(request):
    return render(request, 'shop/prodview.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

