from django.db import models
from django.contrib.auth.models import AbstractUser


class House(models.Model):
    class Meta:
        db_table = 'houses'

    name = models.CharField(unique=True, max_length=255, primary_key=True)
    colour = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Meta:
        db_table = 'users'

    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True)
    dob = models.DateField(default='2003-07-07')  # default value only used for super users
    comments = models.TextField(blank=True)


