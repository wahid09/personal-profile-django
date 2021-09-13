from django.contrib import admin
from django.urls import path
from Blog_App.views import index, getauthor, getsingle, categoryPost, CreateBlog, MyPost

app_name = 'Blog_App'

urlpatterns = [
    path('', index, name='index'),
    path('author/<name>', getauthor, name="post_author"),
    path('article/<int:id>', getsingle, name="single_post"),
    path('category/<name>', categoryPost, name="category_post"),
    path('create-article', CreateBlog.as_view(), name="create_blog"),
    path('list-article', MyPost.as_view(), name="my_blog")
]