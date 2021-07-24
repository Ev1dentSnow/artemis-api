from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = 'users'

    dob = models.DateField(default='2003-07-07')  # default value only used for super users
    comments = models.TextField(blank=True)
