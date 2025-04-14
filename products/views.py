from django.shortcuts import render
from .models import Post


# Create your views here.


def products(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'products/products.html', {'posts':posts})