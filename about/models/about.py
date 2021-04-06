from django.db import models

class About(models.Model):
    name = models.CharField(max_length= 30, null=False)
    designation = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    email = models.EmailField(max_length=254)
    objective = models.TextField()
    active = models.BooleanField(default=False)

