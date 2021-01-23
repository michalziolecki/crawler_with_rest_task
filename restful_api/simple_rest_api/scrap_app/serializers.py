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
