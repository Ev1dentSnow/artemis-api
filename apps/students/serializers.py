from rest_framework import serializers, status
from rest_framework.response import Response

from apps.students.models import Student
from apps.users.models import User


class BasicUserSerializer(serializers.ModelSerializer):  # For user creation
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'dob', 'first_name', 'last_name', 'comments')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    user = BasicUserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            dob=user_data['dob'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            comments=user_data['comments']
        )
        user.set_password(user_data['password'])
        user.save()

        student = Student.objects.create(
            user_id=user.id,
            form=validated_data['form'],
            enrollment_year=validated_data['enrollment_year']
        )
        return student
