from django.db import models


class ResumeAnalysis(models.Model):
    resume = models.OneToOneField(
        "resumes.Resume",
        on_delete=models.CASCADE,
        related_name="analysis"
    )
    summary = models.TextField(blank=True, null=True)
    skills = models.JSONField(default=list)
    experience_level = models.CharField(max_length=100, blank=True, null=True)
    suggestions = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for Resume {self.resume_id}"