from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

@login_required(login_url='signin')
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username, email= email , password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id,)
                new_profile.save()
                messages.success(request,'Account Created Successfully!!!')
                return redirect('signup')
        else:
            messages.error(request,'Password Not Matching')
            return redirect('signup')
    else:
     return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            messages.error(request,'Invalid Credentials')
            return redirect('signin')

    return render(request,'signin.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully!!!')
    return redirect('signin')