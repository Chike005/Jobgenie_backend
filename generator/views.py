from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeRequest


def _format_resume(data: dict) -> str:
    full_name = data.get("full_name", "Your Name")
    email = data.get("email", "")
    phone = data.get("phone", "")
    education = data.get("education", [])
    projects = data.get("projects", [])
    work_history = data.get("work_history", [])
    skills = data.get("skills", [])

    lines = [full_name]
    contact = " | ".join([p for p in [email, phone] if p]).strip()
    if contact:
        lines.append(contact)
    lines.append("")

    if education:
        lines.append("Education")
        for e in education:
            lines.append(
                f"- {e.get('degree','')} – {e.get('institution','')}, "
                f"{e.get('location','')} ({e.get('date','')})"
            )
        lines.append("")

    if projects:
        lines.append("Projects")
        for p in projects:
            lines.append(f"- {p.get('name','')} ({p.get('date','')})")
            if p.get("problem"):
                lines.append(f"  Problem: {p['problem']}")
            if p.get("tools"):
                lines.append(f"  Tools: {', '.join(p['tools'])}")
            for h in p.get("highlights", []):
                lines.append(f"  • {h}")
        lines.append("")

    if work_history:
        lines.append("Work History")
        for w in work_history:
            lines.append(f"- {w.get('role','')} – {w.get('org','')} ({w.get('date','')})")
            for b in w.get("bullets", []):
                lines.append(f"  • {b}")
        lines.append("")

    if skills:
        lines.append("Skills")
        lines.append(", ".join(skills))
        lines.append("")

    return "\n".join(lines).strip()

@api_view(["POST"])
def generate_resume(request):
    serializer = ResumeRequest(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    resume_text = _format_resume(serializer.validated_data)
    return Response({"resume": resume_text}, status=status.HTTP_200_OK)
