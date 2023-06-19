from rest_framework import serializers
from sentiment.models import Analysis
class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ('text',)