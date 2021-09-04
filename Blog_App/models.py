from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from stdimage import StdImageField, JPEGField

# Create your models here.


def validate_image(image):
    max_height = 600
    max_width = 500
    height = image.file.height
    width = image.file.width
    if width > max_width or height > max_height:
        raise ValidationError("Height or Width is larger than what is allowed")


class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    details = RichTextField(blank=True, null=True)
    author_image = StdImageField(upload_to='author_images/%Y/%m/', variations={'thumbnail': {'width': 100, 'height': 75}})
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
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    articate_image = StdImageField(upload_to='blog_images/%Y/%m/', variations={
        'large': (1200, 600),
        'thumbnail': (500, 300, True),
    }, delete_orphans=True)
    publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.title

