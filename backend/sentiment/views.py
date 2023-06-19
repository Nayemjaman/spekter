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

        sentiment_classifier = pipeline('sentiment-analysis')

        result = sentiment_classifier(text)[0]
        sentiment = result['label']


        # Download from Hub and run inference
        # model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
        # # Run inference
        # preds = model([text])
        # sentiment = "positive" if preds[0].item() == 1 else "negative"

        return Response({'sentiment': sentiment})
    

class UnregisteredUserTokenView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Generate a token for unregistered users
        token = self.get_token(self.get_user(request))

        # Return the token as the response
        return Response({'token': str(token.access_token)})