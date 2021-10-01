from rest_framework import serializers

from apps.assignments.models import Assignment
from apps.classes.models import Classes
from apps.marks.models import Marks
from apps.students.models import Student


class MarksInputSerializer(serializers.Serializer):
    assignment_id = serializers.IntegerField()
    class_id = serializers.IntegerField()
    student_id = serializers.IntegerField()
    mark_awarded = serializers.DecimalField(max_digits=19, decimal_places=1)

    def validate_assignment_id(self, assignment_id):
        """
        Check that the assignment id exists
        """
        if not Assignment.objects.filter(id=assignment_id).exists():
            raise serializers.ValidationError('assignment id does not exist')
        return assignment_id

    def validate_class_id(self, class_id):
        """
        Check that the class id exists
        """
        if not Classes.objects.filter(id=class_id).exists():
            raise serializers.ValidationError('class id does not exist')
        return class_id

    def validate_student_id(self, student_id):
        """
        Check that the student id exists
        """
        if not Student.objects.filter(pk=student_id):
            raise serializers.ValidationError('student id does not exist')
        return student_id

    def validate(self, data):
        """
        Check that mark for specified assignment + student does not already exist
        """
        if Marks.objects.filter(student_id=data['student_id'], assignment_id=data['assignment_id']).exists():
            raise serializers.ValidationError('mark already exists for this assignment id and this student id')
        return data

    def create(self, validated_data):
        new_mark = Marks.objects.create(assignment_id=validated_data['assignment_id'],
                                        class_id_id=validated_data['class_id'],
                                        student_id=validated_data['student_id'],
                                        mark_awarded=validated_data['mark_awarded'])
        return new_mark


