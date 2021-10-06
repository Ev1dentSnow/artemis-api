from rest_framework import serializers

from apps.assignments.models import Assignment
from apps.teachers.serializers import TeacherSerializer


class AssignmentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    assignment_name = serializers.CharField()
    max_marks = serializers.DecimalField(max_digits=19, decimal_places=1)
    date_assigned = serializers.DateField()
    date_due = serializers.DateField()
    teacher = TeacherSerializer()

    def create(self, validated_data):
        new_assignment = Assignment.objects.create(assignment_name=validated_data['assignment_name'],
                                                   max_marks=validated_data['max_marks'],
                                                   date_assigned=validated_data['date_assigned'],
                                                   date_due=validated_data['date_due'],
                                                   teacher_id=validated_data['teacher']['user_id'])
        return new_assignment
