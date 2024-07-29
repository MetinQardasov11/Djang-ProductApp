from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.

def index(request):
    context = {
        'products' : Product.objects.filter(is_active=True, is_bestseller=True),
        'categories' : Category.objects.all()
    }
    return render(request, 'Product/index.html', context)

def products(request):
    context = {
        'products' : Product.objects.filter(is_active=True),
        'categories' : Category.objects.all()
    }
    return render(request, 'Product/products.html', context)

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    
    return render(request, 'Product/product_detail.html', {
        'product': product
    })

def category_detail(request, slug):
    context = {
        'products' : Category.objects.get(slug=slug).product_set.all().filter(is_active=True),
        'categories' : Category.objects.all(),
        'selected_category' : slug
    }
    return render(request, 'Product/products.html', context)