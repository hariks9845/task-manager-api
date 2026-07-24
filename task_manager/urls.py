from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Simple view for root path
def api_root(request):
    return JsonResponse({
        "message": "Task Manager API is Live!",
        "endpoints": {
            "tasks": "/api/tasks/",
            "categories": "/api/categories/",
            "optimized_schedule": "/api/tasks/optimized-schedule/",
            "token_auth": "/api/auth/token/"
        }
    })

urlpatterns = [
    path('', api_root),  # Handles root '/'
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Replace with your app name if different
]