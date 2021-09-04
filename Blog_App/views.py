from django.shortcuts import render, HttpResponse, get_object_or_404
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
    post = get_object_or_404(Article, pk=id )
    first = Article.objects.first()
    last = Article.objects.last()
    context = {
        "post": post,
        "first": first,
        "last": last
    }
    return render(request, 'blog/single.html', context)

def categoryPost(request, name):
    pass
