from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient
from rest_framework import status

from .models import Task
from .scheduler import TaskSchedulerEngine

class TaskSchedulerAlgorithmTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        now = timezone.now()

        self.task_low = Task.objects.create(
            title="Low priority task",
            priority=Task.Priority.LOW,
            due_date=now + timedelta(days=1),
            owner=self.user
        )
        self.task_critical = Task.objects.create(
            title="Critical task",
            priority=Task.Priority.CRITICAL,
            due_date=now + timedelta(days=2),
            owner=self.user
        )
        self.task_medium = Task.objects.create(
            title="Medium task",
            priority=Task.Priority.MEDIUM,
            due_date=now + timedelta(hours=5),
            owner=self.user
        )

    def test_min_heap_scheduler_ordering(self):
        engine = TaskSchedulerEngine()
        queryset = Task.objects.filter(owner=self.user)
        scheduled_tasks = engine.build_schedule(queryset)

        # Critical (1) -> Medium (3) -> Low (4)
        self.assertEqual(scheduled_tasks[0].id, self.task_critical.id)
        self.assertEqual(scheduled_tasks[1].id, self.task_medium.id)
        self.assertEqual(scheduled_tasks[2].id, self.task_low.id)


class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        response = self.client.post('/api/auth/token/', {
            'username': 'testuser',
            'password': 'password123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_get_optimized_schedule_endpoint(self):
        response = self.client.get('/api/tasks/optimized-schedule/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('schedule', response.data)
        self.assertEqual(response.data['algorithm'], 'Min-Heap Priority Queue')