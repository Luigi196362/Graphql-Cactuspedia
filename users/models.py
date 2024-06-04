from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.TextField(default="https://th.bing.com/th/id/R.da23698789163cd86b5926cb55febc91?rik=lQ3tuFTKGq8YTw&riu=http%3a%2f%2fgetdrawings.com%2fimage%2fcute-cactus-drawing-56.jpg&ehk=yCYuKpvbrcGogPfx5fF6miInOgx1qmTSwHOu3%2fqYUgg%3d&risl=&pid=ImgRaw&r=0")
    is_premium = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
