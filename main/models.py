from django.db import models
from django.utils import timezone


# Create your models here.

class VideoUrl(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    downloaded = models.BooleanField(default=False)
    date =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
