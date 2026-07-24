from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

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
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/', include('task_manager.urls')),  # <-- Make sure 'api.urls' matches your app folder name!
]