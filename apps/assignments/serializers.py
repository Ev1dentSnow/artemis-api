from rest_framework import serializers

from apps.assignments.models import Assignment


class AssignmentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    assignment_name = serializers.CharField()
    max_marks = serializers.DecimalField(max_digits=19, decimal_places=1)
    date_assigned = serializers.DateField()
    date_due = serializers.DateField()
    teacher_id = serializers.IntegerField()