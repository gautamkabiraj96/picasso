from django.urls import path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Picaso API",
        default_version="v1",
        description="API documentation for Picaso API",
        terms_of_service="https://www.example.com",
        contact=openapi.Contact(email="habitsofpicasso@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('tasks/', include('tasks.urls')),
    path('users/', include('users.urls')),
    
    # swagger ui
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # raw json
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
