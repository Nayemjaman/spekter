from rest_framework import generics
from rest_framework.response import Response
from sentiment.serializers import AnalysisSerializer
from transformers import pipeline

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny


class SentimentAnalysisView(generics.CreateAPIView):
    serializer_class = AnalysisSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data['text']
        sentiment_classifier = pipeline(
            "sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        result = sentiment_classifier(text)
        label = result[0]['label']
        sentiment = label.lower()
        return Response({'sentiment': sentiment})


class UnregisteredUserTokenView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        token = self.get_token(self.get_user(request))
        return Response({'token': str(token.access_token)})
