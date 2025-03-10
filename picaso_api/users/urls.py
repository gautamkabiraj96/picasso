from django.urls import path
from .views import UserListCreateView, UserDetailView, SignupView, LoginView, TokenRefreshView, LogoutView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path("signup", SignupView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    path("renew", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout", LogoutView.as_view(), name="logout"),
]
