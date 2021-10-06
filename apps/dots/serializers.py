from rest_framework import serializers

from apps.dots.models import Dots
from apps.teachers.serializers import BasicTeacherUserDetailsSerializer, TeacherSerializer, TeacherDotsSerializer


class DotsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    reason = serializers.CharField()
    student_id = serializers.IntegerField()
    assigning_teacher = TeacherDotsSerializer()

    def create(self, validated_data):
        new_dot = Dots.objects.create(reason=validated_data['reason'],
                                      student_id=validated_data['student_id'],
                                      assigning_teacher_id=validated_data['assigning_teacher']['id'])
        return new_dot

