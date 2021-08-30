from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'app_login/login.html')


def signup(request):
    form = UserCreationForm()
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form, 'registered': registered}
    return render(request, 'App_Login/signup.html', context=dict)
