from django.db import models

class SocialLink(models.Model):
    linked_id = models.CharField(max_length=254, null=True)
    github_link = models.CharField(max_length=254, null=True)
    tweeter_link = models.CharField(max_length=254, null=True)
    facebook_link = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.linked_id