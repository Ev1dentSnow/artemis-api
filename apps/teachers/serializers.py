from django.contrib.auth.models import Group
from rest_framework import serializers

from apps.teachers.models import Teacher
from apps.users.models import User, House
from apps.users.serializers import BasicUserSerializer


class TeacherSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    subject = serializers.ReadOnlyField()

class TeacherDotsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    subject = serializers.ReadOnlyField()

class BasicTeacherUserDetailsSerializer(serializers.Serializer):
    user_details = BasicUserSerializer(source='user')

class TeacherListSerializer(serializers.Serializer):
    user_details = BasicUserSerializer(source='user')
    subject = serializers.CharField()

    def create(self, validated_data):
        # password is the same as the username if a password is not supplied
        if 'password' not in validated_data['user']:
            validated_data['user']['password'] = validated_data['user']['username']

        # When creating a user we can't just provide the house name, the "create_user" method requires a house instance
        validated_data['user']['house'] = House.objects.get(name=validated_data['user']['house'])
        new_user = User.objects.create_user(**validated_data['user'])
        teacher = Teacher.objects.create(user_id=new_user.id, subject=validated_data['subject'])
        teacher_group = Group.objects.get(name='teachers')
        new_user.groups.add(teacher_group)
        return teacher

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
            user_house_instance = House.objects.get(name=user_details.get('house', user.house))
            user.house = user_house_instance
            user.comments = user_details.get('comments', user.comments)
            user.save()

        if student_details is not None:
            instance.subject = validated_data.get('subject', instance.subject)
            instance.save()

        return instance



