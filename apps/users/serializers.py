from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.response import Response

from apps.users.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class BasicUserSerializer(serializers.Serializer):  # For user creation

    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    dob = serializers.DateField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    comments = serializers.CharField()



