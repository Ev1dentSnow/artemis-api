from rest_framework import serializers

from apps.teachers.models import Teacher


class TeacherSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    subject = serializers.ReadOnlyField()
