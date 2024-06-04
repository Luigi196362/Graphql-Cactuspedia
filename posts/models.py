from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    
    postUser = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    postText = models.TextField(null=True)
    postImage = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
