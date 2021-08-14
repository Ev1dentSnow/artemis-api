from rest_framework import serializers
from apps.classes.models import Classes


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
