from django.db import models
from ckeditor.fields import RichTextField


class Experience(models.Model):
    position = models.CharField(max_length=100, null=False)
    company_name = models.CharField(max_length=254, null=False)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    till_now = models.BooleanField(default=False)
    job_description = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.position