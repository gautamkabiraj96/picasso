from django.urls import path
from .views import UserListCreateView, UserDetailView, RegisterView, LoginView, UserView, GoogleLoginView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('google', GoogleLoginView.as_view(), name='google_login'),
    path('me', UserView.as_view(), name='user_details'),
]
