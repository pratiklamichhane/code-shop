from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , "home/index.html")

def home(request):
    
    return render(request , "home/base.html", {'user':request.user})