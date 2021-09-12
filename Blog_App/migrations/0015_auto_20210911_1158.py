# Generated by Django 3.2.6 on 2021-09-11 05:58

import ckeditor.fields
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0014_article_publish_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='article',
            name='articate_image',
            field=stdimage.models.StdImageField(upload_to='blog_images/%Y/%m/', verbose_name='Article Image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=254, verbose_name='Title'),
        ),
    ]
