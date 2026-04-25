from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import ResumeUploadSerializer



from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Resume
from .serializers import ResumeUploadSerializer


class ResumeUploadAPIView(CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeUploadSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]