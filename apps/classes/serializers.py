from rest_framework import serializers
from apps.classes.models import Classes
from apps.classes.models import StudentClasses
from apps.students.serializers import BasicStudentUserDetailsSerializer
from apps.teachers.models import TeacherClasses
from apps.teachers.serializers import BasicTeacherUserDetailsSerializer


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClasses
        fields = '__all__'


class BasicTeacherClassesSerializer(serializers.ModelSerializer):
    """
    Used to assign a teacher to a class
    """

    class Meta:
        model = TeacherClasses
        fields = '__all__'


class StudentClassesSerializer(serializers.Serializer):
    """
    Used to view class details and a list of students in the classes
    """
    classs = ClassSerializer(source='class_id')
    student = BasicStudentUserDetailsSerializer(source='student_id')
