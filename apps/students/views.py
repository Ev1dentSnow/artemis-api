from django.http import Http404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

import artemisapi.permissions as permissions
from apps.classes.models import Classes, StudentClasses
from apps.dots.models import Dots
from apps.dots.serializers import DotsSerializer
from apps.marks.models import Marks
from apps.marks.serializers import MarksInputSerializer
from apps.students.models import Student
from apps.students.serializers import StudentSerializer, StudentInstanceClassSerializer, StudentInstanceMarksSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import User


class ArtemisTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token


class ArtemisTokenObtainPairView(TokenObtainPairView):
    serializer_class = ArtemisTokenObtainPairSerializer


class StudentInstanceView(APIView):
    permission_classes = (permissions.isAuthenticated | permissions.isAdmin,)
    serializer_class = StudentSerializer

    def get(self, request, student_user_id):
        """
        Fetch one student
        """
        student = Student.objects.filter(user_id=student_user_id)
        serializer = StudentSerializer(student, many=True)
        if student:  # checking if queryset is empty
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, student_user_id):
        """
        Modify student details
        :param request:
        :param student_user_id:
        :return: Response
        """
        student = Student.objects.get(user_id=student_user_id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, student_user_id):
        """
        Permanently delete student and their user details
        :param request:
        :param student_user_id:
        :return: Response
        """
        student = Student.objects.get(user_id=student_user_id)
        user = User.objects.get(id=student_user_id)
        student.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentInstanceClassesView(APIView):
    permission_classes = (permissions.isOwner | permissions.isTeacher | permissions.isAdmin,)

    def get(self, request, student_user_id):
        """
        Get a list of classes a specific student is in
        """
        class_ids = []
        for student_class in StudentClasses.objects.filter(student_id=student_user_id):
            class_ids.append(Classes.objects.get(id=student_class.class_id_id))
        serializer = StudentInstanceClassSerializer(class_ids, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentInstanceDotsView(APIView):
    permission_classes = (permissions.isOwner | permissions.isTeacher | permissions.isAdmin,)

    def get(self, request, student_user_id):
        """
        Get a list of a specific student's dots
        """
        dots = Dots.objects.filter(student_id=student_user_id)
        serializer = DotsSerializer(dots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, student_user_id):
        """
        Add a new dot to a student
        """
        serializer = DotsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'dot created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentInstanceDotsInstanceView(APIView):
    permission_classes = (permissions.isOwner | permissions.isTeacher | permissions.isAdmin,)

    def delete(self, request, student_user_id, dot_id):
        """
        Delete a student's dot
        """
        dot = Dots.objects.get(pk=dot_id)
        dot.delete()
        return Response({'detail': 'dot removed successfully'}, status=status.HTTP_204_NO_CONTENT)


class StudentInstanceMarksListView(APIView):
    permission_classes = (permissions.isOwner | permissions.isTeacher | permissions.isAdmin,)

    def get(self, request, student_user_id):
        """
        Get a list of a specific student's marks
        """
        marks_list = []
        marks = Marks.objects.select_related('assignment').filter(student_id=student_user_id)
        for mark in marks:
            marks_list.append(mark)
        serializer = StudentInstanceMarksSerializer(marks_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, student_user_id):
        """
        Assign a mark for a specific assignment to a specific student
        """
        serializer = MarksInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'mark assigned successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentInstanceMarksInstanceView(APIView):
    permission_classes = (permissions.isOwner | permissions.isTeacher | permissions.isAdmin,)

    def get(self, request, student_user_id, mark_id):
        """
        Get a specific mark that belongs to a specific student
        """
        mark = Marks.objects.get()
        serializer = StudentInstanceMarksSerializer(mark)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, student_user_id, mark_id):
        """
        Modify a specific mark that belongs to a specific student
        """
        mark = Marks.objects.get(id=mark_id, student_id=student_user_id)
        serializer = StudentInstanceMarksSerializer(mark, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, student_user_id, mark_id):
        mark = Marks.objects.get(id=mark_id, student_id=student_user_id)
        mark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
