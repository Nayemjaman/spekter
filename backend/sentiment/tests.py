from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from sentiment.models import Analysis


class SentimentAnalysisTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_sentiment_analysis_positive(self):
        text = "I love this product!"
        response = self.client.post(
            '/api/analyze/', {'text': text}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sentiment'], 'positive')

    def test_sentiment_analysis_negative(self):
        text = "This movie is terrible!"
        response = self.client.post(
            '/api/analyze/', {'text': text}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sentiment'], 'negative')
