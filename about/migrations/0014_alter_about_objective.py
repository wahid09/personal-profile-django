# Generated by Django 3.2.6 on 2021-08-31 16:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_prifileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='objective',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
