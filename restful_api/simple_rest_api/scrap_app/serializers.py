from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import WebAddress, ImageData, TextData


class WebAddressSerializer(ModelSerializer):
    class Meta:
        model = WebAddress
        fields = [
            'uuid',
            'link'
        ]
        read_only_fields = [
            'id',
            'uuid',
        ]


class ImageDataSerializer(ModelSerializer):
    related_web_addr = serializers.UUIDField(source='related_web_addr.uuid', read_only=True)

    class Meta:
        model = ImageData
        fields = [
            'uuid',
            'related_web_addr',
            'alt',
            'src'
        ]
        read_only_fields = [
            'id',
            'uuid',
        ]


class TextDataSerializer(ModelSerializer):
    related_web_addr = serializers.UUIDField(source='related_web_addr.uuid', read_only=True)

    class Meta:
        model = TextData
        fields = [
            'uuid',
            'related_web_addr',
            'text'
        ]
        read_only_fields = [
            'id',
            'uuid',
        ]
