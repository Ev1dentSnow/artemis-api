from rest_framework import serializers, status
from rest_framework.response import Response

from apps.students.models import Student
from apps.users.models import User
from apps.users.serializers import BasicUserSerializer


class StudentSerializer(serializers.Serializer):
    user_details = BasicUserSerializer(source='user')  # source is the actual name of the field
    form = serializers.IntegerField()
    enrollment_year = serializers.IntegerField()
