from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/', include('ProjectAPI.urls')),
    path('api/users/', include('UserAPI.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
