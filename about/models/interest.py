from django.db import models

class Interest(models.Model):
    interest = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.interest