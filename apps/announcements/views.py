from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AnnouncementsList(APIView):

    def get(self, request):
        return Response('', status=status.HTTP_200_OK)
