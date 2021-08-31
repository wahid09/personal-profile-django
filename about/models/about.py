from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    name = models.CharField(max_length= 30, null=False)
    designation = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    email = models.EmailField(max_length=254)
    objective = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

