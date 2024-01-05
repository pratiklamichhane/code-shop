from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
# Create your views here.


def get_products(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/products.html', {'product': product})