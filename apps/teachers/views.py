from django.shortcuts import render
from rest_framework.views import APIView

from ArtemisAPI import permissions
from apps.teachers.serializers import BasicTeacherUserDetailsSerializer
from apps.users.models import User


