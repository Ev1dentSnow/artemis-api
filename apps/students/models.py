from django.db import models

import apps.users.models


class Student(models.Model):
    class Meta:
        db_table = 'students'

    user = models.OneToOneField(apps.users.models.User, on_delete=models.CASCADE, primary_key=True)
    form = models.IntegerField()
    enrollment_year = models.IntegerField()
