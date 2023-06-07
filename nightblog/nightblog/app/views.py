from django.shortcuts import render
from .models import *


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'posts': posts, 'categories': categories})

def category_post(request, id):
    category = Category.objects.get(id=id)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'index.html', {'posts': posts, 'categories': categories})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    categories = Category.objects.all()
    return render(request, 'post.html', {'post': post, 'categories': categories})