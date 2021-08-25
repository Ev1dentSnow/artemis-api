from django.db import models

from apps.students.models import Student
from apps.teachers.models import Teacher
from apps.users.models import User


class Dots(models.Model):
    class Meta:
        db_table = 'dots'

    reason = models.CharField(null=False, max_length=256, default=None)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assigning_teacher = models.ForeignKey(User, on_delete=models.CASCADE)

