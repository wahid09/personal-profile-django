from django.db import models

class Skills(models.Model):
    backend_language = models.CharField(max_length=254, null=True, blank=True)
    backend_framwork = models.CharField(max_length=254, null=True, blank=True)
    frontend_language = models.CharField(max_length=254, null=True, blank=True)
    frontend_framwork = models.CharField(max_length=254, null=True, blank=True)
    database = models.CharField(max_length=254, null=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.backend_language