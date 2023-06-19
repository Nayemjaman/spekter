from django.urls import path
from sentiment.views import SentimentAnalysisView

urlpatterns = [
    path('analyze/', SentimentAnalysisView.as_view(), name='analyze'),
]