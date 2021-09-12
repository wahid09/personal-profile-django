# Generated by Django 3.2.6 on 2021-09-10 13:50

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A positive (A+)'), ('A-', 'A negative (A-)'), ('B+', 'B RhD positive (B+)'), ('B-', 'B negative (B-)'), ('O+', 'O positive (O+)'), ('O-', 'O RhD negative (O-)'), ('AB+', 'AB RhD positive (AB+)'), ('AB-', 'AB RhD negative (AB-)')], default=django.utils.timezone.now, max_length=3, verbose_name='Blood Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=stdimage.models.StdImageField(upload_to='profile_images/%Y/%m/', verbose_name='Profile Image'),
        ),
    ]