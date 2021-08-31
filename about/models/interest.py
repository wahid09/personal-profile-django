from django.db import models
from ckeditor.fields import RichTextField


class Interest(models.Model):
    interest = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.interest