from django.urls import path
from .views import generate_resume , generate_resume_docx

urlpatterns = [
    path('generate_resume/', generate_resume, name='generate_resume'),
    path('generate_resume_docx/', generate_resume_docx, name='generate_resume_docx'),
]
