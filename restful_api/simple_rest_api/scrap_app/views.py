import subprocess

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .filters import ImageDataFilterSet, TextDataFilterSet
from .serializers import WebAddressSerializer, ImageDataSerializer, TextDataSerializer
from .models import WebAddress, ImageData, TextData
import os


class WebAddressViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = WebAddress.objects.all()
    serializer_class = WebAddressSerializer
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['link']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url: str = serializer.data.get('link', None)
        if not url or not url.startswith('http'):
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST,
                            headers={'result': 'fail', 'info': 'bad input'})
        shell_result = self.run_scraper(url)
        if shell_result != 0:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST,
                            headers={'result': 'fail', 'info': 'scraper bad status',
                                     'scraper status': f'{shell_result}'})
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers={'result': 'success'})

    def run_scraper(self, url):
        scraper_path = os.path.join(settings.SEMANTIVE_DIR, 'scraper', 'data_scraper.py')
        command = f'python {scraper_path} -l {url} -t -i'
        return os.system(command)


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
