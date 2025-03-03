from rest_framework import serializers
from .models import Task  # Import the Task model from the models module

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify which model to serialize
        model = Task
        # Use '__all__' to automatically include all fields from the Task model in the serializer
        fields = '__all__'
