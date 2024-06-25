from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('ProjectAPI.urls')),
    path('api/users/', include('UserAPI.urls')),
    path('admin/', admin.site.urls),
]
