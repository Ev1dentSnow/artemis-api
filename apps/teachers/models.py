from django.db import models
from django.db.models import CASCADE

import apps.users.models


class Teacher(models.Model):
    class Meta:
        db_table = 'teachers'

        user = models.OneToOneField(apps.users.models.User, on_delete=CASCADE, primary_key=True)
        subject = models.CharField()
