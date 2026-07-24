from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Landing page response for root URL "/"
def api_root(request):
    return JsonResponse({
        "status": "online",
        "message": "Task Manager API is Live!",
        "endpoints": {
            "admin": "/admin/",
            "api_root": "/api/",
            "tasks": "/api/tasks/",
            "categories": "/api/categories/",
            "optimized_schedule": "/api/tasks/optimized-schedule/"
        }
    })

urlpatterns = [
    path('', api_root),  # Handles the root "/" path!
    path('admin/', admin.site.urls),
    path('api/', include('scheduler_api.urls')),
]