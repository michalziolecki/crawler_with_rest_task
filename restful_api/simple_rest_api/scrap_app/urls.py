from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import WebAddressViewSet, ImageDataViewSet, TextDataViewSet

app_name = 'scrap_app'

urlpatterns = [
]

router = SimpleRouter()
router.register('web-address', WebAddressViewSet, basename='webaddress')
router.register('image-data', ImageDataViewSet, basename='imagedata')
router.register('text-data', TextDataViewSet, basename='textdata')

urlpatterns += router.urls
