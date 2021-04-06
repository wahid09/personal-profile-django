from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=254, null=False)
    technologies = models.CharField(max_length=254, null=False)
    short_note = models.TextField()
    live_url = models.CharField(max_length=254)