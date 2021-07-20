from rest_framework import serializers

from apps.quotes.models import Quote


class QuoteSerializer(serializers.Serializer):

    quote = serializers.CharField()
    author = serializers.CharField()

