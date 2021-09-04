from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.teachers.models import Teacher, TeacherClasses
from artemisapi import permissions
from apps.teachers.serializers import BasicTeacherUserDetailsSerializer, TeacherListSerializer
from apps.users.models import User


class TeachersListView(APIView):
    permission_classes = (permissions.isAdmin,)
    serializer_class = TeacherListSerializer

    def get(self, request):
        """
        Fetches a list of teachers
        """
        teachers = Teacher.objects.all()
        serializer = TeacherListSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new teacher
        """
        serializer = TeacherListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'teacher created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherInstanceView(APIView):
    permission_classes = (permissions.isOwner | permissions.isAdmin,)

    def get(self, request, teacher_user_id):
        """
        Fetch one teacher
        """
        teacher = Teacher.objects.filter(user_id=teacher_user_id)
        serializer = TeacherListSerializer(teacher, many=True)
        if teacher:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, teacher_user_id):
        """
        Modify teacher details
        """
        teacher = Teacher.objects.get(user_id=teacher_user_id)
        serializer = TeacherListSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, teacher_user_id):
        """
        Permanently delete teacher and their user details
        """
        teacher = Teacher.objects.get(user_id=teacher_user_id)
        user = User.objects.get(id=teacher_user_id)
        teacher.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherClassesView(APIView):
    permission_classes = (permissions.isOwner | permissions.isAdmin,)

    def get(self, request, teacher_user_id):
        """
        Fetches a list of classes a specific teacher teaches
        """
        classes = TeacherClasses.objects.select_related('teacher_id', 'class_id_id').filter(teacher_id=teacher_user_id)
