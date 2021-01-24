from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .filters import ImageDataFilterSet, TextDataFilterSet
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
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['alt', 'src']
    filterset_class = ImageDataFilterSet


class TextDataViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = TextData.objects.all()
    serializer_class = TextDataSerializer
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['text']
    filterset_class = TextDataFilterSet
