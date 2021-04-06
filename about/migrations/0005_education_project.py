# Generated by Django 3.1.7 on 2021-04-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20210405_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=254)),
                ('institute', models.CharField(max_length=254)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('till_now', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=254)),
                ('technologies', models.CharField(max_length=254)),
                ('short_note', models.TextField()),
                ('live_url', models.CharField(max_length=254)),
            ],
        ),
    ]
