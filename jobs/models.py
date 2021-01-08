# https://docs.djangoproject.com/en/2.0/ref/models/fields/
from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)