from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    reviewcount=models.IntegerField(default=0)
    nickname=models.CharField(max_length=10, null=True)
