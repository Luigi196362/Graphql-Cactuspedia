from django.db import models
from django.conf import settings

# Create your models here.
class Game(models.Model):
    gameName = models.TextField()
    gameDescription = models.TextField()
    gameIcon = models.TextField()
    gameImage = models.TextField()

