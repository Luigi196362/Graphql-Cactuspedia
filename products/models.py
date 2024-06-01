from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    stock=  models.IntegerField()
    description = models.TextField()
    image = models.TextField()

