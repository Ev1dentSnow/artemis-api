from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        db_table = 'users'

    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=80)
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    dob = models.DateField()
    role = models.TextField()
    house = models.TextField()
    comments = models.TextField()
