
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from django.http import *
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import *


from django.conf import settings

# Create your views here.



def register(request):
    
    try:
        # print(request.method)
        if request.method == 'POST':
            name = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('c_password')
            # print(name,email,password , confirm_password)
            if name and email and password and confirm_password:
                user = User(username = name,email=email,password=password)
                user.save()
                return redirect('login_save')
    except:
        return redirect('register')

    return render(request , 'register.html')



def login_save(request):
    try:
        if request.method == "POST":
            print(request.method)
            name = request.POST.get('username')
            password = request.POST.get('password')
            print(name,password)
            
            user = authenticate(username = name,  password=password)
            if user is not None:
                login(request , user)
                
                return redirect('dashboard')
    except:
        print('got the error user not login')
        return redirect('login_save')
    return render(request , 'login.html')
def logout_user(request):
    try:
        if request.user.is_authenticated:

            user = request.user
            logout(request)
            
            return redirect('login_save')
    except:
        print('error user not logout')
        return redirect('dashboard')

# @login_required(login_url="login_save")
def dashbord(request):
    data = User.objects.all()
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    # s=SessionStore()
    # s.save()
    # s.session_key
    # if settings.SESSION_EXPIRE_AT_BROWSER_CLOSE:
    #     max_age = None
    #     expires = None
    # s.set_expiry()

    
    return render(request , 'dashboard.html',{'data':data})