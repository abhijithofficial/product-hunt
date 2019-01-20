from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['cpassword']:
             try:
                 user = User.objects.get(username=request.POST['username'])
                 if user is not None:
                     error="Username already exist"
                     return render(request,'account/signup.html',{'error':error})
             except User.DoesNotExist:
                 user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                 auth.login(request,user)
                 return redirect('home')
        else:
            error = "Confirm Password is not correct"
            return render(request,'account/signup.html',{'error':error})
    else:
        return render(request,'account/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if  user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            error="Invalid password or username"
            return render (request,'account/login.html',{'error':error})

    else:
        return render(request,'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
