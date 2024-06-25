from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt import authentication
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="TeamColab Management System API",
        default_version='v1',
        description="A comprehensive project management system to manage users, projects, tasks, and comments efficiently. This system allows users to register, login, create and manage projects and tasks, and collaborate through comments.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(authentication.JWTAuthentication,),
)

urlpatterns = [
    path('api/', include('ProjectAPI.urls')),
    path('api/users/', include('UserAPI.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('swagger-doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
