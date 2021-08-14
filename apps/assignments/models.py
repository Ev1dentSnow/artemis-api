from django.db import models
from django.db.models import CASCADE

import apps.teachers.models


class Assignment(models.Model):
    class Meta:
        db_table = 'assignments'

    id = models.IntegerField(primary_key=True)
    teacher = models.OneToOneField(apps.teachers.models.Teacher, on_delete=CASCADE)
    name = models.CharField(max_length=256)
    max_marks = models.DecimalField(max_digits=3, decimal_places=1)
    date_assigned = models.DateTimeField()
    date_due = models.DateTimeField()
