# core/urls.py
from django.urls import path
from . import views
from generator.views import generate_resume

urlpatterns = [
    path('generate-resume/', views.generate_resume, name='generate_resume'),
    path('generate-cover-letter/', views.generate_cover_letter, name='generate_cover_letter'),
   
]
