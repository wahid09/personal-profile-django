from django.db import models

class Education(models.Model):
    degree_name = models.CharField(max_length=254, null=False)
    subject_name = models.CharField(max_length=254, null=True, blank=True)
    institute = models.CharField(max_length=254, null=False)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    till_now = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.degree_name