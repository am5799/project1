from django.http import HttpResponse
from django.template import loader
from .models import Post, Comment, Category
from django.contrib.auth.models import User
from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)

def blogs(request):
    blogs = Post.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)

def blog_details(request, id):
    blog = Post.objects.get(id=id)
    template = loader.get_template('blogdetails.html')
    context = {'blog': blog}
    return HttpResponse(template.render(context, request))

def comments(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'comments.html', context)

def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories.html', context)
