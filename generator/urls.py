from django.urls import path
from .views import generate_resume

urlpatterns = [
    path('generate_resume/', generate_resume, name='generate_resume'),
]
