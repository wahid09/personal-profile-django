# Generated by Django 3.1.7 on 2021-04-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linked_id', models.CharField(max_length=254, null=True)),
                ('github_link', models.CharField(max_length=254, null=True)),
                ('tweeter_link', models.CharField(max_length=254, null=True)),
                ('facebook_link', models.CharField(max_length=254, null=True)),
            ],
        ),
    ]
