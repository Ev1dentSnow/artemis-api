from rest_framework import serializers
from apps.classes.models import Classes
from apps.classes.models import StudentClasses


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClasses
        fields = '__all__'
