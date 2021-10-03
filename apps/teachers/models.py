from django.db import models
from django.db.models import CASCADE

import apps.users.models
import apps.classes.models


class Teacher(models.Model):
    class Meta:
        db_table = 'teachers'

    user = models.OneToOneField(apps.users.models.User, on_delete=CASCADE, primary_key=True)
    subject = models.CharField(max_length=256)


class TeacherClasses(models.Model):
    class Meta:
        db_table = 'teacher_classes'

    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    class_id = models.OneToOneField(apps.classes.models.Classes, on_delete=models.CASCADE)
