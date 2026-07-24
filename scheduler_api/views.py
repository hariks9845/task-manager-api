from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from .scheduler import TaskSchedulerEngine

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['get'], url_path='optimized-schedule')
    def get_optimized_schedule(self, request):
        pending_tasks = self.get_queryset().filter(is_completed=False)
        
        engine = TaskSchedulerEngine()
        scheduled_tasks = engine.build_schedule(pending_tasks)

        serializer = self.get_serializer(scheduled_tasks, many=True)
        return Response({
            "count": len(scheduled_tasks),
            "algorithm": "Min-Heap Priority Queue",
            "schedule": serializer.data
        }, status=status.HTTP_200_OK)