from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_images', verbose_name="Profile Image")
    phone_number = models.CharField(max_length=11, verbose_name='Phone Number', null=True, blank=True)
    active = models.BooleanField(default=False)
