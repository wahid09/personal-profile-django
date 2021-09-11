from django.shortcuts import HttpResponse, HttpResponseRedirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Blog_App.forms import SignUpForm


# Create your views here.


def getLogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Blog_App:index'))
    else:
        # if request.method == "POST":
        #     user = request.POST.get('user')
        #     password = request.POST.get('pass')
        #     auth = authenticate(request, username=user, password=password)
        #     if auth is not None:
        #         login(request, auth)
        #         return redirect('Blog_App:index')
        #     else:
        #         messages.info(request, 'invalid credentials')
        #         return redirect('Blog_App:login')
        form = AuthenticationForm()
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('Login_App:user_account'))
    return render(request, "app_login/login.html", context={'form': form})


@login_required
def user_account(request):
    return render(request, "app_login/user_profile.html")


@login_required
def getLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Blog_App:index'))


def user_register(request):
    form = SignUpForm()
    registered = False
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            return HttpResponseRedirect(reverse('Login_App:login'))
    dict = {'form': form, 'registered': registered}
    return render(request, 'app_login/signup.html', context=dict)
