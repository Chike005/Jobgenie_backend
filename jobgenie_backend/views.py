from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def generate_resume(request):
    if request.method != "POST":
        return JsonResponse({"detail":"Method Not Allowed"}, status=405)
    return JsonResponse({"ok": True, "msg": "Job Genie is alive"})
