from django.db import models

import apps.users.models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    class Meta:
        db_table = 'students'

    user = models.OneToOneField(apps.users.models.User, on_delete=models.CASCADE, primary_key=True)
    form = models.IntegerField()
    enrollment_year = models.IntegerField()
