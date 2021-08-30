import json

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from artemisapi.permissions import isAuthenticated
from apps.quotes import models
from apps.quotes.models import Quote
from apps.quotes.serializers import QuoteSerializer


class QuoteView(APIView):

    permission_classes = (isAuthenticated,)

    def get(self, request):

        file = open('apps/quotes/daily_quote.json')
        json_data = json.load(file)

        quote = json_data[0]['q']
        author = json_data[0]['a']

        q = Quote(quote, author)
        serializer = QuoteSerializer(q)
        return Response(serializer.data)
