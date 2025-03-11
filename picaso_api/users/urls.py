from django.urls import path
from .views import UserListCreateView, UserView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('me', UserView.as_view(), name='user_details'),
]
