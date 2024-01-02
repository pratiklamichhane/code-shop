from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)
        if not user_obj.exists():
            messages.warning(request, "User Doesn't Exists")
            return HttpResponseRedirect(request.path_info)
        
        # if not user_obj[0].profile.is_email_verified:
        #     messages.warning(request, "Your account is not verified , please check your mail and verify it")
        #     return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = username , password = password)
        if user_obj:
            login(request , user_obj)
            return redirect("/")


        messages.warning(request, 'Invalid credentials.')
        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/login.html')

def signup_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)
        if user_obj.exists():
            messages.warning(request, "Username is already Taken , Try another")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name = first_name , last_name = last_name , username = username , email = email )
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'Account has been created , Go to login page and login into your account.')
        return HttpResponseRedirect(request.path_info)
    
    return render(request , 'accounts/signup.html')