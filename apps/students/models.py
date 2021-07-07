from django.db import models

import apps.users.models


class Student(models.Model):
    class Meta:
        db_table = 'students'

    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(apps.users.models.User, on_delete=models.CASCADE)
    form = models.IntegerField()
    enrollment_year = models.IntegerField()
