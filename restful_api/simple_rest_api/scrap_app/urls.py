from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import WebAddressViewSet, ImageDataViewSet, TextDataViewSet

app_name = 'scrap_app'

urlpatterns = [
]

# router = SimpleRouter()
# router.register('scrap_app', WebAddressViewSet, basename='webaddress')
# router.register('scrap_app', ImageDataViewSet, basename='imagedata')
# router.register('scrap_app', TextDataViewSet, basename='textdata')

# urlpatterns += router.urls
