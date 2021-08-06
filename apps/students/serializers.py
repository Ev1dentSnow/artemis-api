from django.contrib.auth.models import Group
from rest_framework import serializers, status
from rest_framework.response import Response

from apps.students.models import Student
from apps.users.models import User
from apps.users.serializers import BasicUserSerializer


class StudentSerializer(serializers.Serializer):
    user_details = BasicUserSerializer()  # source is the actual name of the field

    form = serializers.IntegerField()
    enrollment_year = serializers.IntegerField()
    primary_contact_name = serializers.CharField()
    primary_contact_email = serializers.EmailField()
    secondary_contact_name = serializers.CharField()
    secondary_contact_email = serializers.EmailField()

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data['user'])
        student = Student.objects.create(user_id=new_user.id, form=validated_data['form'],
                                         enrollment_year=validated_data['enrollment_year'],
                                         primary_contact_name=validated_data['primary_contact_name'],
                                         primary_contact_email=validated_data['primary_contact_email'],
                                         secondary_contact_name=validated_data['secondary_contact_name'],
                                         secondary_contact_email=validated_data['secondary_contact_email']
                                         )

        student_group = Group.objects.get(name='students')
        new_user.groups.add(student_group)
        return student

    def update(self, instance, validated_data):
        user_details = validated_data.pop('user_details', None)
        student_details = validated_data

        if user_details is not None:
            for item in user_details:
                instance.item = item[item]
