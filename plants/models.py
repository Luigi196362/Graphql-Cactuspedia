from django.db import models
from django.conf import settings

# Create your models here.
class Plant(models.Model):
    plantName = models.TextField()
    plantType = models.TextField()
    plantOrigin=models.TextField()
    plantDescription = models.TextField()
    plantImage = models.TextField()

