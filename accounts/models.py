from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255,blank=True)
    address = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return self.username

