from django.contrib import admin
from .models import Task, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'priority', 'due_date', 'is_completed')
    list_filter = ('priority', 'is_completed')
    search_fields = ('title', 'description')