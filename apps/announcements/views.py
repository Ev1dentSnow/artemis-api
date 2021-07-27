from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ArtemisAPI_django.permissions import isStudent, isAuthenticated
from apps.announcements.models import Announcement
from apps.announcements.serializers import AnnouncementSerializer


class AnnouncementsListView(APIView):

    permission_classes = (isAuthenticated,)  # Any authenticated user can view the announcements

    def get(self, request):
        announcements = Announcement.objects.all()  # select all announcements in db
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnnouncementInstanceView(APIView):

    permission_classes = (isAuthenticated,)

    def get(self, request, announcement_id):
        announcement = Announcement.objects.filter(id=announcement_id)
        serializer = AnnouncementSerializer(announcement, many=True)  # Find out why many=True is necessary
        if announcement:  # checking if queryset is empty
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise NotFound(detail='announcement with that id does not exist')  # if id not found
