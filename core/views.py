import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .utils.generate_resume import create_resume

@csrf_exempt
@require_http_methods(["POST"])
def generate_resume(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    doc_bytes = create_resume(payload)
    filename = f'{payload.get("name","resume").replace(" ", "_")}_resume.docx'
    resp = HttpResponse(
        doc_bytes,
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    resp["Content-Disposition"] = f'attachment; filename="{filename}"'
    return resp
