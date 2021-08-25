from rest_framework import serializers

from apps.teachers.models import Teacher


class TeacherSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    subject = serializers.ReadOnlyField()


class BasicTeacherUserDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
