from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.students.models import Student
from apps.students.serializers import StudentSerializer


class StudentsList(APIView):

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
