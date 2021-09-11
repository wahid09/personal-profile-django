from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, redirect
from Blog_App.models import Article, Author, Category
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
#from django.urls import reverse
#from django.contrib.auth.decorators import login_required
#from Blog_App.forms import SignUpForm


# Create your views here.

def index(request):
    blogs = Article.objects.all()
    # Search
    search = request.GET.get('search')
    if search:
        blogs = blogs.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    # pagnation
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
    post = get_object_or_404(Article, pk=id)
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


# def getLogin(request):
#     if request.user.is_authenticated:
#         return redirect('Blog_App:index')
#     else:
#         # if request.method == "POST":
#         #     user = request.POST.get('user')
#         #     password = request.POST.get('pass')
#         #     auth = authenticate(request, username=user, password=password)
#         #     if auth is not None:
#         #         login(request, auth)
#         #         return redirect('Blog_App:index')
#         #     else:
#         #         messages.info(request, 'invalid credentials')
#         #         return redirect('Blog_App:login')
#         form = AuthenticationForm()
#         if request.method == "POST":
#             form = AuthenticationForm(data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get('username')
#                 password = form.cleaned_data.get('password')
#                 user = authenticate(username=username, password=password)
#
#                 if user is not None:
#                     login(request, user)
#                     return HttpResponseRedirect(reverse('Blog_App:user_account'))
#     return render(request, "blog/login.html", context={'form': form})
#
#
# @login_required
# def user_account(request):
#     # user = request.user.all()
#     # print(user)
#     return render(request, "blog/user_profile.html")
#
#
# @login_required
# def getLogout(request):
#     logout(request)
#     return redirect('Blog_App:index')
#
#
# def user_register(request):
#     form = SignUpForm()
#     registered = False
#     if request.method == "POST":
#         form = SignUpForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             registered = True
#             return HttpResponseRedirect(reverse('Blog_App:login'))
#     dict = {'form': form, 'registered': registered}
#     return render(request, 'blog/register.html', context=dict)
