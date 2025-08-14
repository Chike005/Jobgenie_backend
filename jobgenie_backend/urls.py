from django.contrib import admin
from django.urls import path
from .views import generate_resume

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/generate_resume/", generate_resume),
]
