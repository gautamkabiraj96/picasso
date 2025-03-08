from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, hello_world

router = DefaultRouter()
router.register('', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
