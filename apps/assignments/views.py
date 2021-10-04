from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.assignments.models import Assignment
from apps.assignments.serializers import AssignmentSerializer
from artemisapi import permissions


class AssignmentsListView(APIView):

    permission_classes = (permissions.isTeacher | permissions.isAdmin,)

    def get(self, request):
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'assignment created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


