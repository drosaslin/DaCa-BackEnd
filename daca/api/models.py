from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    gender = models.CharField(max_length=6)
    birthday = models.DateField(default=date.min)
    password = models.CharField(max_length=60)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'gender', 'birthday', 'password']