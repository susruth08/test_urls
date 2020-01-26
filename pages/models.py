from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class LcmUrl(models.Model):
    url_string = models.TextField(null=False, blank=False, unique=True)
    numbers = ArrayField(ArrayField(models.IntegerField()))
