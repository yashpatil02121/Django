from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password Didn't Match!")
        else:
            newUser = User.objects.create_user(username, email, password1)
            newUser.save()
            return redirect('login')
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Username or Password doesn't Match, or User Does not Exists")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')