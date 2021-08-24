# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        usena = request.POST['username']
        firna = request.POST['first_name']
        lasna = request.POST['last_name']
        emai = request.POST['email']
        passw = request.POST['password']
        passw1 = request.POST['password1']
        if passw == passw1:
            if User.objects.filter(username=usena).exists():
                messages.info(request, "Username already Exist")
                return redirect('/credentials/')
            elif User.objects.filter(email=emai).exists():
                messages.info(request, "Email ID already registered")
                return redirect('/credentials')
            else:
                user = User.objects.create_user(username=usena, password=passw, first_name=firna, last_name=lasna,
                                                email=emai)
                user.save()
                print('user created')
                user = auth.authenticate(username=usena, password=passw)
                if user is not None:
                    auth.login(request, user)
                    # return redirect('/')
                    return render(request, "welcome.html")
        else:
            messages.info(request, "password mismatch")
            return redirect('/credentials')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        usr = request.POST['username']
        psw = request.POST['password']
        user = auth.authenticate(username=usr, password=psw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/credentials/login/')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
