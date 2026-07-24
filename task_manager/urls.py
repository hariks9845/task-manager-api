from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "Task Manager API is running!"})

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/', include('scheduler_api.urls')),  # <-- Pointing to scheduler_api!
]