# Generated by Django 3.2.6 on 2021-09-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_App', '0002_auto_20210910_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A positive (A+)'), ('A-', 'A negative (A-)'), ('B+', 'B RhD positive (B+)'), ('B-', 'B negative (B-)'), ('O+', 'O positive (O+)'), ('O-', 'O RhD negative (O-)'), ('AB+', 'AB RhD positive (AB+)'), ('AB-', 'AB RhD negative (AB-)')], default='A+', max_length=3, verbose_name='Blood Group'),
        ),
    ]
