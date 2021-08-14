from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import ArtemisAPI_django.permissions as permissions
from apps.classes.models import Classes
from apps.classes.serializers import ClassSerializer


class ClassesListView(APIView):
    permission_classes = (permissions.isTeacher | permissions.isAdmin,)
    serializer_class = ClassSerializer

    def get(self, request):
        """
        Get all classes
        """
        classes = Classes.objects.all()
        serializer = ClassSerializer(classes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create new class
        """
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'class created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
