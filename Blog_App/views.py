from django.shortcuts import render, HttpResponse
from Blog_App.models import Article, Author, Category

# Create your views here.

def index(request):
    blogs = Article.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, "blog/index.html", context)

def getauthor(request, name):
    return render(request, 'blog/profile.html')

def getsingle(request, id):
    return render(request, 'blog/single.html')
