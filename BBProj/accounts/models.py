from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #id = username으로 대체, password는 그대로
    name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=128)
    location_city = models.CharField(max_length=64)
    location_gu = models.CharField(max_length=64)

