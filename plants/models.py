from django.db import models
from django.conf import settings

# Create your models here.
class Plant(models.Model):
    name = models.TextField()
    type = models.TextField()
    origin=models.TextField()
    description = models.TextField()
    image = models.TextField()

