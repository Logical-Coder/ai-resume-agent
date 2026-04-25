from rest_framework import serializers

from .models import Resume
from .services import ResumeParserService
from .services import AIResumeService
from apps.ai_agent.services import AIResumeService
from apps.ai_agent.models import ResumeAnalysis

class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = [
            "id",
            "candidate_name",
            "resume_file",
            "extracted_text",
            "uploaded_at",
        ]
        read_only_fields = ["id", "extracted_text", "uploaded_at"]

    
    def create(self, validated_data):
        resume = Resume.objects.create(**validated_data)

        try:
            extracted_text = ResumeParserService.extract_text_from_pdf(
                resume.resume_file.path
            )

            resume.extracted_text = extracted_text
            resume.save(update_fields=["extracted_text"])

            ai_result = AIResumeService.analyze_resume(extracted_text)

            ResumeAnalysis.objects.create(
                resume=resume,
                summary=ai_result["summary"],
                skills=ai_result["skills"],
                experience_level=ai_result["experience_level"],
                suggestions=ai_result["suggestions"],
            )

        except Exception as e:
            resume.extracted_text = f"Error: {str(e)}"
            resume.save(update_fields=["extracted_text"])

        return resume