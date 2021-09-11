from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField, JPEGField
from ckeditor.fields import RichTextField

# Create your models here.

class UserProfile(models.Model):
    GROUP_CHOICES = (
        ('A+', 'A positive (A+)'),
        ('A-', 'A negative (A-)'),
        ('B+', 'B RhD positive (B+)'),
        ('B-', 'B negative (B-)'),
        ('O+', 'O positive (O+)'),
        ('O-', 'O RhD negative (O-)'),
        ('AB+', 'AB RhD positive (AB+)'),
        ('AB-', 'AB RhD negative (AB-)'),
    )
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    #profile_pic = models.ImageField(upload_to='profile_images', verbose_name="Profile Image")
    profile_pic = StdImageField(upload_to='profile_images/%Y/%m/', variations={'thumbnail': {'width': 600, 'height': 600}}, verbose_name="Profile Image")
    phone_number = models.CharField(max_length=11, verbose_name='Phone Number', null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=GROUP_CHOICES, verbose_name="Blood Group", default='A+')
    about = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
