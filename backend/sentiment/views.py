from django.shortcuts import render


from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from transformers import pipeline
# Create your views here.
class SentimentAnalysisView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        text = request.data.get('text')
        if not text:
            return Response({'error': 'Text is required.'}, status=400)

        # Perform sentiment analysis using a pre-trained model
        sentiment_classifier = pipeline('sentiment-analysis')
        result = sentiment_classifier(text)[0]
        sentiment = result['label']

        return Response({'sentiment': sentiment})
