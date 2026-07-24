from rest_framework import serializers
from .models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'category', 'category_name', 
            'owner', 'priority', 'due_date', 'estimated_hours', 
            'is_completed', 'created_at'
        ]

    def validate_priority(self, value):
        if value not in [1, 2, 3, 4]:
            raise serializers.ValidationError("Priority must be between 1 (Critical) and 4 (Low).")
        return value