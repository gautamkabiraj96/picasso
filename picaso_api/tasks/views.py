from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, Django REST Framework!"})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
