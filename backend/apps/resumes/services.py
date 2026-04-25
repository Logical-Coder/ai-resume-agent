from pypdf import PdfReader


class ResumeParserService:
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        text = ""

        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text.strip()
class AIResumeService:

    @staticmethod
    def analyze_resume(text: str):
        text_lower = text.lower()

        skills = []

        if "python" in text_lower:
            skills.append("Python")
        if "django" in text_lower:
            skills.append("Django")
        if "flask" in text_lower:
            skills.append("Flask")
        if "aws" in text_lower:
            skills.append("AWS")
        if "docker" in text_lower:
            skills.append("Docker")

        experience = "Unknown"

        if "7+" in text:
            experience = "Senior (7+ years)"

        return {
            "skills": skills,
            "experience": experience,
            "summary": "Experienced backend developer with strong system design skills."
        }