from django.urls import path
from .views import ResumeAnalysisDetailAPIView
from .views import ResumeJobMatchAPIView

urlpatterns = [
    path("resume-analysis/<int:pk>/", ResumeAnalysisDetailAPIView.as_view()),
    path("match/", ResumeJobMatchAPIView.as_view()),
]