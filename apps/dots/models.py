from django.db import models

from apps.students.models import Student
from apps.teachers.models import Teacher


class Dots(models.Model):
    class Meta:
        db_table = 'dots'

    reason = models.CharField(null=False, max_length=256, default=None)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assigning_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

