from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenRefreshView
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication URLs
    re_path('api/auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('tasks/', include('tasks.urls')),
    # path('users/', include('users.urls')),
]
