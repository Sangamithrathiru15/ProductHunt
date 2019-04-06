from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['pwd']==request.POST['confirmpwd']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'User name already taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['pwd'])
                auth.login(request,user)
                return redirect('homepage')
        else:
            return render(request,'accounts/signup.html',{'error':'pwd doesnt match'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == "POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['pwd'])
        if user is not None:
            auth.login(request,user)
            return redirect('homepage')
        else:
            return render(request,'accounts/login.html',{'error':'Username/ password is wrong'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('homepage')
    