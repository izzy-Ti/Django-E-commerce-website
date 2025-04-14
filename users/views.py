from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

def login_user(request):
    user_aut = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request=request, username = username, password=password)
        if user is not None:
            login(request, user)
            user_aut = True
            return redirect('home')
        else:
            messages.error(request, '*Invalid username or password')
            return redirect('users:login')
    return render(request, 'users/login.html')
def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error (request, "*Username already exists")
        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error (request, "*Email already exists")
        if len(password) < 5 :
            user_data_has_error = True
            messages.error (request, "*Password must be atleast 5 characters")
        if not user_data_has_error :
            new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password,
            )
            messages.success (request, "Account have successfully created")
            return redirect('users:login')
        else:
            return redirect('users:signup')

    return render(request, 'users/signin.html')
