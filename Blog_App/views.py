from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from Blog_App.models import Article, Author, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def index(request):
    blogs = Article.objects.all()
    #Search
    search = request.GET.get('search')
    if search:
        blogs = blogs.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    #pagnation
    paginator = Paginator(blogs, 12)  # Show 25 contacts per page.
    page_number = request.GET.get('p')
    total_article = paginator.get_page(page_number)

    categories = Category.objects.all()
    context = {
        'blogs': total_article,
        'categories': categories
    }
    return render(request, "blog/index.html", context)

def getauthor(request, name):
    author = get_object_or_404(User, username=name)
    auth = get_object_or_404(Author, name=author.id)
    posts = Article.objects.filter(article_author=auth.id)

    paginator = Paginator(posts, 12)  # Show 25 contacts per page.
    page_number = request.GET.get('p')
    posts = paginator.get_page(page_number)
    context = {
        "auth": auth,
       "posts": posts
    }
    return render(request, 'blog/profile.html', context)

def getsingle(request, id):
    post = get_object_or_404(Article, pk=id )
    first = Article.objects.first()
    last = Article.objects.last()
    related_post = Article.objects.filter(category=post.category).exclude(id=id)[:4]
    context = {
        "post": post,
        "first": first,
        "last": last,
        "related": related_post
    }
    return render(request, 'blog/single.html', context)

def categoryPost(request, name):
    category = get_object_or_404(Category, name=name)
    posts = Article.objects.filter(category=category.id)

    paginator = Paginator(posts, 12)  # Show 25 contacts per page.
    page_number = request.GET.get('p')
    posts = paginator.get_page(page_number)

    categories = Category.objects.all()
    context = {
        "category": category,
        "posts": posts,
        "categories": categories
    }
    return render(request, "blog/category_post.html", context)


def getLogin(request):
    if request.user.is_authenticated:
        return redirect('Blog_App:index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('Blog_App:index')
    return render(request, "blog/login.html")


def getLogout(request):
    logout(request)
    return redirect('Blog_App:index')
