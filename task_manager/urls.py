from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"status": "API is online", "docs": "/api/tasks/"})

urlpatterns = [
    path('', home_view),  # Handles the root '/' URL
    path('admin/', admin.site.urls),
    path('api/', include('your_app_name.urls')), # Replace with your app name
]