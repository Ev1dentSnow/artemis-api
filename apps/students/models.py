from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.TextField()
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    dob = models.DateField()
    role = models.TextField()
    house = models.TextField()
    comments = models.TextField()


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.IntegerField()
    enrollment_year = models.IntegerField()


class Announcement(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.TextField()
    content = models.TextField()
