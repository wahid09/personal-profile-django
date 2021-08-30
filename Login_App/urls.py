from django.contrib import admin
from django.urls import path, include
from Login_App import views
from .views import home

app_name = 'Login_App'

urlpatterns = [
    path('', home, name="home"),
    path('signup/', views.signup, name="signup"),
]