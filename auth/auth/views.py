from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        email=request.POST['email']
        pass1 =request.POST['password']
        pass2 =request.POST['cpassword']
        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')
def Login(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        pass1 =request.POST['pass']
        us=authenticate(username=uname,password=pass1)
        if us is not None:
            login(request, us)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!")


    return render(request,'login.html')
def forgot(request):
    return render(request,'forgot.html')
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')