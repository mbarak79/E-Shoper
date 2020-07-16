from django.shortcuts import render
from settings.models import Brand
from .models import Product

# Create your views here.


def index(request):
    brands = Brand.objects.all()
    products = Product.objects.all()

    context = {
        'brands': brands,
        'products': products
    }
    return render(request, 'index.html', context)



def shop(request):
    return render(request, 'shop.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')