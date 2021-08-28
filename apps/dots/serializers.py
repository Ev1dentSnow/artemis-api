from rest_framework import serializers

from apps.dots.models import Dots
from apps.teachers.serializers import BasicTeacherUserDetailsSerializer


class DotsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    reason = serializers.CharField()
    student_id = serializers.IntegerField()
    assigning_teacher = BasicTeacherUserDetailsSerializer()
