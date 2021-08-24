from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import json

from ArtemisAPI.permissions import isAuthenticated


class WeatherView(APIView):

    permission_classes = (isAuthenticated,)

    def get(self, request):
        file = open('apps/weather/weather_data.json')
        json_data = json.loads(file.read())
        file.close()
        return Response(json_data)
