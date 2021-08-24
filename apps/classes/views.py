from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import ArtemisAPI.permissions as permissions
from apps.classes.models import Classes, StudentClasses
from apps.classes.serializers import ClassSerializer, StudentClassSerializer


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


class StudentClassesListView(APIView):
    permission_classes = (permissions.isTeacher | permissions.isAdmin,)
    serializer_class = StudentClassSerializer

    def get(self, request):
        """
        Get a list of students and the classes they are in (ID only)
        """
        student_classes = StudentClasses.objects.all()
        serializer = StudentClassSerializer(student_classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Add a student to a class
        """
        serializer = StudentClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'student added to class successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)