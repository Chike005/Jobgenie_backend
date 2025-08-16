from django.contrib import admin
from django.urls import path, include
from .views import health, home

urlpatterns = [
    path('', home),                      # root page
    path('admin/', admin.site.urls),
    path('api/health/', health),         # health check
    path('api/', include('generator.urls')),
]
