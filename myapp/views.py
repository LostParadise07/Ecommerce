from django.http import HttpResponse
#  render template
from django.shortcuts import render
from .models import Category, Subcategory


def index(request):
    categories = Category.objects.prefetch_related('subcategories').all()
    
    return render(request, "shopify/index.html", context={'categories': categories})

def about(request):
    return render(request, "shopify/about.html")

def contact(request):
    return render(request, "shopify/contact.html")

def products(request):
    return render(request, "shopify/products.html")

def single_product(request):
    return render(request, "shopify/single-product.html")


