from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class BasicUserSerializer(serializers.Serializer):  # For user creation

    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.EmailField()
    dob = serializers.DateField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    comments = serializers.CharField()

