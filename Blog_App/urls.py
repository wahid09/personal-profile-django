from django.contrib import admin
from django.urls import path
from Blog_App.views import index, getauthor, getsingle

app_name = 'Blog_App'

urlpatterns = [
    path('', index, name='index'),
    path('author/<name>', getauthor, name="author"),
]