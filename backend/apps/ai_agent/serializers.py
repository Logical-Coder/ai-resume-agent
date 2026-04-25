from rest_framework import serializers
from .models import ResumeAnalysis


class ResumeAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeAnalysis
        fields = [
            "id",
            "resume",
            "summary",
            "skills",
            "experience_level",
            "suggestions",
            "created_at",
        ]