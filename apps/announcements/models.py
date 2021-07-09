from django.db import models


class Announcement(models.Model):

    class Meta:
        db_table = 'announcements'

    id = models.AutoField(primary_key=True)
    subject = models.TextField()
    content = models.TextField()
