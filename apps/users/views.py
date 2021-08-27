from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ArtemisAPI import permissions
from apps.users.models import User
from apps.users.serializers import UniqueDetailsSerializer


class UsersListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UniqueDetailsSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
