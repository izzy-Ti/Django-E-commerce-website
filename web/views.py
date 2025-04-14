from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def front(request):
    return render(request, 'front.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')