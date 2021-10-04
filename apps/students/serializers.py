from django.contrib.auth.models import Group
from rest_framework import serializers, status
from rest_framework.response import Response

from apps.assignments.serializers import AssignmentSerializer
from apps.classes.models import Classes
from apps.students.models import Student
from apps.users.models import User, House
from apps.users.serializers import BasicUserSerializer


class BasicStudentUserDetailsSerializer(serializers.Serializer):
    user_details = BasicUserSerializer(source='user')


class StudentSerializer(serializers.Serializer):
    user_details = BasicUserSerializer(source='user')  # source is the actual name of the field in the model

    form = serializers.IntegerField()
    enrollment_year = serializers.IntegerField()
    primary_contact_name = serializers.CharField()
    primary_contact_email = serializers.EmailField()
    secondary_contact_name = serializers.CharField()
    secondary_contact_email = serializers.EmailField()

    def create(self, validated_data):
        # password is the same as the username if a password is not supplied
        if 'password' not in validated_data['user']:
            validated_data['user']['password'] = validated_data['user']['username']

        validated_data['user']['house'] = House.objects.get(name=validated_data['user']['house'])
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
        user_details = validated_data.pop('user', None)
        student_details = validated_data

        if user_details is not None:
            user = User.objects.get(id=instance.user_id)
            user.username = user_details.get('username', user.username)
            user.set_password(user_details.get('password', user.password))
            user.first_name = user_details.get('first_name', user.first_name)
            user.last_name = user_details.get('last_name', user.last_name)
            user.email = user_details.get('email', user.email)
            user.dob = user_details.get('dob', user.dob)
            user.email = user_details.get('email', user.email)
            user.house = user_details.get('house', user.house)
            user.comments = user_details.get('comments', user.comments)
            user.save()

        if student_details is not None:
            instance.form = validated_data.get('form', instance.form)
            instance.enrollment_year = validated_data.get('enrollment_year', instance.enrollment_year)
            instance.primary_contact_name = validated_data.get('primary_contact_name', instance.enrollment_year)
            instance.primary_contact_email = validated_data.get('primary_contact_email', instance.primary_contact_email)
            instance.secondary_contact_name = validated_data.get('secondary_contact_name',
                                                                 instance.secondary_contact_name)
            instance.secondary_contact_email = validated_data.get('secondary_contact_email',
                                                                  instance.secondary_contact_email)
            instance.save()

        return instance


class StudentInstanceClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id', 'name', 'graduation_date']


class StudentInstanceMarksSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    assignment = AssignmentSerializer()
    mark_awarded = serializers.DecimalField(decimal_places=1, max_digits=19)
    class_id = serializers.IntegerField(source='class_id_id')

    def update(self, instance, validated_data):
        instance.mark_awarded = validated_data.get('mark_awarded', instance.mark_awarded)
        instance.save()
        return instance
