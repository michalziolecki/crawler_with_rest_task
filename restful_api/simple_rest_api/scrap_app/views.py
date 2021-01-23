from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .serializers import WebAddressSerializer, ImageDataSerializer, TextDataSerializer
from .models import WebAddress, ImageData, TextData


class WebAddressViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = WebAddress.objects.all()
    serializer_class = WebAddressSerializer
    lookup_field = 'uuid'


class ImageDataViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer
    lookup_field = 'uuid'


class TextDataViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = TextData.objects.all()
    serializer_class = TextDataSerializer
    lookup_field = 'uuid'
