from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    productName = models.TextField()
    productPrice = models.IntegerField()
    productStock=  models.IntegerField()
    productDescription = models.TextField()
    productImage = models.TextField()

