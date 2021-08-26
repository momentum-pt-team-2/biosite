from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(blank=True, null=True)
    name = models.TexFieldField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True, max_length=14)
    skills = models.TextField(blank=True, null=True)
