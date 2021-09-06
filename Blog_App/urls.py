from django.contrib import admin
from django.urls import path
from Blog_App.views import index, getauthor, getsingle, categoryPost, getLogin, getLogout

app_name = 'Blog_App'

urlpatterns = [
    path('', index, name='index'),
    path('author/<name>', getauthor, name="author"),
    path('article/<int:id>', getsingle, name="single_post"),
    path('category/<name>', categoryPost, name="category_post"),
    path('login', getLogin, name="login"),
    path('logout', getLogout, name="logout"),
]