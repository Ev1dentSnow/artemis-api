from django.http import Http404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

import ArtemisAPI_django.permissions as permissions
from apps.students.models import Student
from apps.students.serializers import StudentSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class ArtemisTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token


class ArtemisTokenObtainPairView(TokenObtainPairView):
    serializer_class = ArtemisTokenObtainPairSerializer


class StudentInstanceView(APIView):
    serializer_class = StudentSerializer

    def get(self, request, student_user_id):
        student = Student.objects.filter(user=student_user_id)
        serializer = StudentSerializer(student, many=True)
        if student:  # checking if queryset is empty
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise Http404


class StudentsListView(APIView):
    permission_classes = (permissions.isAdmin,)

    serializer_class = StudentSerializer

    def get(self, request):
        """
        Get all students
        """
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create new student
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'student created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
