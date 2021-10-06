from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from artemisapi import permissions
from apps.dots.models import Dots
from apps.dots.serializers import DotsSerializer


class DotsListView(APIView):
    """
    Gets a list of all dots
    """
    permission_classes = (permissions.isTeacher | permissions.isAdmin,)

    def get(self, request):
        data = Dots.objects.all()
        serializer = DotsSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DotsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'dot created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

