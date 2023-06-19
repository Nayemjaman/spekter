from django.test import TestCase
from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient

# from sentiment.models import Analysis
# # Create your tests here.

# class AnalysisDRFTests(APITestCase):
#     def setUp(self):
#         Analysis.objects.create(text="I love you.")
#         Analysis.objects.create(text="I don't need you.")

from django.test import TestCase
from sentiment.models import Analysis

class AnalysisModelTest(TestCase):
    def setUp(self) -> None:
        Analysis.objects.create(text='I love you.')
        Analysis.objects.create(text='I hate you.')

    def test_analysis(self):
        pos = Analysis.objects.get(text='I love you.')
        neg = Analysis.objects.get(text='I hate you.')
        self.assertEqual(pos.text,'I love you.')
        self.assertEqual(neg.text,'I hate you.')



    # def test_create_analysis(self):
    #     # Create an instance of the Analysis model
    #     analysis = Analysis.objects.create(text='I love you.')

    #     # Assert that the model instance was created successfully
    #     self.assertIsInstance(analysis, Analysis)
    #     self.assertEqual(analysis.text, 'I love you.')

        
    #     analysis = Analysis.objects.create(text='I hate you.')

    #     # Assert that the model instance was created successfully
    #     self.assertIsInstance(analysis, Analysis)
    #     self.assertEqual(analysis.text, 'I hate you.')

    # def test_analysis_str(self):
    #     # Create an instance of the Analysis model
    #     analysis = Analysis.objects.create(text='I hate you.')

    #     # Assert that the __str__ method returns the expected string representation
    #     self.assertEqual(str(analysis), 'I hate you.')
