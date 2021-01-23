from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('scrap_app.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('api-session-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('admin-panel/', admin.site.urls),
    ]
