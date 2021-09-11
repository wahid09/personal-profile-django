from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class SignUpForm(UserCreationForm):
    # GROUP_CHOICES = (
    #     ('A+', 'A positive (A+)'),
    #     ('A-', 'A negative (A-)'),
    #     ('B+', 'B RhD positive (B+)'),
    #     ('B-', 'B negative (B-)'),
    #     ('O+', 'O positive (O+)'),
    #     ('O-', 'O RhD negative (O-)'),
    #     ('AB+', 'AB RhD positive (AB+)'),
    #     ('AB-', 'AB RhD negative (AB-)'),
    # )
    # Email = forms.EmailField(required=True)
    # Blod_Group = forms.ChoiceField(choices=GROUP_CHOICES)
    #About = TextField(blank=True, null=True)
    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')
