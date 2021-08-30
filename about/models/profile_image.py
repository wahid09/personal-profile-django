from django.db import models


class prifileImage(models.Model):
    image = models.ImageField(upload_to='photo')
    active = models.BooleanField(default=False)