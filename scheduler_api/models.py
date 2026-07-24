from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.IntegerChoices):
        CRITICAL = 1, 'Critical'
        HIGH = 2, 'High'
        MEDIUM = 3, 'Medium'
        LOW = 4, 'Low'

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    due_date = models.DateTimeField()
    estimated_hours = models.FloatField(default=1.0)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # DB Indexing for fast lookups
        indexes = [
            models.Index(fields=['priority', 'due_date']),
            models.Index(fields=['owner', 'is_completed']),
        ]

    def __str__(self):
        return f"[{self.get_priority_display()}] {self.title}"