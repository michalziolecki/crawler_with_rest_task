from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import WebAddressViewSet, ImageDataViewSet, TextDataViewSet

app_name = 'scrap_app'

urlpatterns = [
]

router = SimpleRouter()
router.register('scrap-api', WebAddressViewSet, basename='webaddress')
router.register('scrap-api', ImageDataViewSet, basename='imagedata')
router.register('scrap-api', TextDataViewSet, basename='textdata')

urlpatterns += router.urls
