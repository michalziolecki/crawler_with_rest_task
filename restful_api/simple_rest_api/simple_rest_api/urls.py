from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
"""
Doc endpoints:
    A JSON view of your API specification at file-doc/swagger.json
    A YAML view of your API specification at file-doc/swagger.yaml
    A ReDoc view of your API specification at /core-api-doc/
    A swagger-ui view of your API specification at /
"""

schema_view = get_schema_view(
    openapi.Info(
        title='Scraper RESTful API',
        default_version='v1',
        description='API for store and manage data from scrapring',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('scraper-api/', include('scrap_app.urls')),
    url(r'file-doc/swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('core-api-doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('api-session-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('admin-panel/', admin.site.urls),
    ]
