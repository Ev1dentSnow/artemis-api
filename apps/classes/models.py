from django.db import models

import apps.students.models


class Classes(models.Model):
    class Meta:
        db_table = 'classes'

    name = models.CharField(max_length=256)
    students = models.ManyToManyField(apps.students.models.Student, through='StudentClasses')


class StudentClasses(models.Model):
    class Meta:
        db_table = 'student_classes'

    student = models.ForeignKey(apps.students.models.Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
