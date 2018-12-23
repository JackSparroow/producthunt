from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Invalid email or password'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password']==request.POST['cpassword']:
            try:
                user=User.objects.get(username=request.POST['username'])

                return render(request,'signup.html',{'error':'user already exists'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('login')
        else:
            return render(request,'signup.html',{'error':'password does not match'})
    #user have fill out the form
    else:
        return render(request, 'signup.html')

def signout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')