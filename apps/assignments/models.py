from django.db import models
from django.db.models import CASCADE

import apps.teachers.models


class Assignment(models.Model):
    class Meta:
        db_table = 'assignments'

    teacher = models.ForeignKey(apps.teachers.models.Teacher, on_delete=CASCADE)
    assignment_name = models.CharField(max_length=256)
    max_marks = models.DecimalField(max_digits=19, decimal_places=1)
    date_assigned = models.DateField()
    date_due = models.DateField()
