from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# 1. Simple response view for root URL
def api_root(request):
    return JsonResponse({"message": "Task Manager API is running!"})

# 2. Correct URL Patterns
urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # <-- Must point to 'api.urls' (or your app folder name), NOT 'task_manager.urls'
]