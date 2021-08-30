from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.name.username

class Category(models.Model):
    name = models.CharField(max_length=254)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Article(models.Model):
    article_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    articate_image = models.ImageField(upload_to='blog_images')
    publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.title

