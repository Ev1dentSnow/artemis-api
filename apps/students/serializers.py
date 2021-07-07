from rest_framework import serializers, status
from rest_framework.response import Response

from apps.students.models import Student
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        exclude = ('id',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        users = User.objects.create(**user_data)
        users.student.set(validated_data)
        return Response(data='Student created', status=status.HTTP_201_CREATED)
