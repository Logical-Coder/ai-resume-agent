class AIResumeService:

    @staticmethod
    def analyze_resume(text: str):
        text_lower = text.lower()

        skills = []

        skill_keywords = {
            "Python": "python",
            "Django": "django",
            "Flask": "flask",
            "DRF": "drf",
            "REST API": "rest",
            "AWS": "aws",
            "Docker": "docker",
            "MySQL": "mysql",
            "PostgreSQL": "postgresql",
            "Redis": "redis",
            "JWT": "jwt",
            "GitHub Actions": "github actions",
            "Linux": "linux",
        }

        for skill_name, keyword in skill_keywords.items():
            if keyword in text_lower:
                skills.append(skill_name)

        experience_level = "Beginner"

        if "7+" in text or "senior" in text_lower:
            experience_level = "Senior"
        elif "3" in text or "4" in text:
            experience_level = "Mid-Level"

        suggestions = []

        if "docker" not in text_lower:
            suggestions.append("Add Docker deployment experience.")
        if "aws" not in text_lower:
            suggestions.append("Add AWS cloud deployment experience.")
        if "redis" not in text_lower:
            suggestions.append("Add Redis caching experience.")
        if "celery" not in text_lower:
            suggestions.append("Add Celery background task experience.")

        return {
            "summary": "Backend-focused developer with experience in Python, APIs, and scalable systems.",
            "skills": skills,
            "experience_level": experience_level,
            "suggestions": suggestions,
        }
    @staticmethod
    def match_with_job(resume_text: str, job_text: str):
        resume_words = set(resume_text.lower().split())
        job_words = set(job_text.lower().split())

        matched = resume_words.intersection(job_words)
        score = int((len(matched) / len(job_words)) * 100) if job_words else 0

        missing = job_words - resume_words

        return {
            "score": score,
            "matched_keywords": list(matched)[:20],
            "missing_keywords": list(missing)[:20],
        }