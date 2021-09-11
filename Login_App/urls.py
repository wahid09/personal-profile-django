from django.contrib import admin
from django.urls import path, include
from Login_App import views

app_name = 'Login_App'

urlpatterns = [
    #path('', home, name="home"),
    path('login', views.getLogin, name="login"),
    path('logout', views.getLogout, name="logout"),
    path('user-account', views.user_account, name="user_account"),
    path('register', views.user_register, name="user_register")
]