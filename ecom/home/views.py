from django.shortcuts import render
from products.models import Product , ProductImage

# Create your views here.
def index(request):
    context = {'products' :Product.objects.all()}
    return render(request , "home/index.html" , context)

def home(request):
    
    return render(request , "home/base.html", {'user':request.user})