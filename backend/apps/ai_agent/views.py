from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import ResumeAnalysis
from .serializers import ResumeAnalysisSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.resumes.models import Resume
from apps.jobs.models import JobDescription
from .services import AIResumeService


class ResumeAnalysisDetailAPIView(RetrieveAPIView):
    queryset = ResumeAnalysis.objects.all()
    serializer_class = ResumeAnalysisSerializer
    permission_classes = [AllowAny]

class ResumeJobMatchAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        resume_id = request.data.get("resume_id")
        job_id = request.data.get("job_id")

        try:
            resume = Resume.objects.get(id=resume_id)
            job = JobDescription.objects.get(id=job_id)

            result = AIResumeService.match_with_job(
                resume.extracted_text,
                job.description
            )

            return Response(result)

        except Resume.DoesNotExist:
            return Response({"error": "Resume not found"}, status=404)
        except JobDescription.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)