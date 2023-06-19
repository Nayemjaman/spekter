from django.urls import path
from sentiment.views import SentimentAnalysisView, UnregisteredUserTokenView

urlpatterns = [
    path('analyze/', SentimentAnalysisView.as_view(), name='analyze'),
    path('api-token-auth/', UnregisteredUserTokenView.as_view(),
         name='api_token_auth'),
]
