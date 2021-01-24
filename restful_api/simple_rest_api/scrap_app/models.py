from django.db import models
from django.utils import timezone
import datetime
import uuid
from django.db.models.signals import pre_save


class WebAddress(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    link = models.CharField(max_length=2048, null=False, unique=True)
    scraped_text = models.BooleanField(default=False)
    scraped_images = models.BooleanField(default=False)
    validity_term = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'data_webaddress'

    def __str__(self):
        return self.link


class ImageData(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    related_web_addr = models.ForeignKey(WebAddress, on_delete=models.CASCADE)
    alt = models.CharField(max_length=1000, null=False)
    src = models.CharField(max_length=2048, null=False)

    class Meta:
        db_table = 'data_imagedata'

    def __str__(self):
        return self.src


class TextData(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    related_web_addr = models.ForeignKey(WebAddress, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, null=False)

    class Meta:
        db_table = 'data_textdata'

    def __str__(self):
        return self.text


def handle_validity_term(sender, instance, **kwargs):
    if not WebAddress.objects.filter(uuid=instance.uuid).exists():
        instance.validity_term = timezone.now() + datetime.timedelta(days=1)


pre_save.connect(handle_validity_term, sender=WebAddress)
