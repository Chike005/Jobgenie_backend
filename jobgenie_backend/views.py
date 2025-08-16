from django.http import JsonResponse, HttpResponse

def health(request):
    return JsonResponse({"ok": True, "msg": "Job Genie is alive"})

def home(request):
    return HttpResponse("JobGenie Backend ✓ Try /api/health/ or POST /api/generate_resume/")
