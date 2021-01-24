from django_filters import FilterSet
from .models import ImageData, TextData


class ImageDataFilterSet(FilterSet):
    class Meta:
        model = ImageData
        fields = ['related_web_addr__uuid', 'related_web_addr__link']


class TextDataFilterSet(FilterSet):
    class Meta:
        model = TextData
        fields = ['related_web_addr__uuid', 'related_web_addr__link']
