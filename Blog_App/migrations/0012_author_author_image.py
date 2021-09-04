# Generated by Django 3.2.6 on 2021-09-04 15:55

from django.db import migrations
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0011_alter_article_articate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_image',
            field=stdimage.models.StdImageField(default=django.utils.timezone.now, upload_to='author_images/%Y/%m/'),
            preserve_default=False,
        ),
    ]