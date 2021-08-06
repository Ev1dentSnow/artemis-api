from django.db import models
from django.db.models import CASCADE

import apps.users.models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    class Meta:
        db_table = 'students'

    user = models.OneToOneField(apps.users.models.User, on_delete=CASCADE, primary_key=True)
    form = models.IntegerField()
    enrollment_year = models.IntegerField()
    primary_contact_name = models.CharField(null=True, max_length=256, default=None)
    primary_contact_email = models.CharField(null=True, max_length=256, default=None)
    secondary_contact_name = models.CharField(null=True, max_length=256, default=None)
    secondary_contact_email = models.CharField(null=True, max_length=256, default=None)
