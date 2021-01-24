from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import WebAddressViewSet, ImageDataViewSet, TextDataViewSet

app_name = 'scrap_app'

urlpatterns = [
]

router = SimpleRouter()
router.register('web-address-api', WebAddressViewSet, basename='webaddress')
router.register('image-data-api', ImageDataViewSet, basename='imagedata')
router.register('text-data-api', TextDataViewSet, basename='textdata')

urlpatterns += router.urls
