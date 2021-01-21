from django.db import models
import uuid


class WebAddress(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    link = models.CharField(max_length=2048, null=False, unique=True)

    def __str__(self):
        return self.link


class ImageData(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    related_web_addr = models.ForeignKey(WebAddress, on_delete=models.CASCADE)
    alt = models.CharField(max_length=1000, null=False, unique=True)
    src = models.CharField(max_length=2048, null=False, unique=True)

    def __str__(self):
        return self.src


class TextData(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    related_web_addr = models.ForeignKey(WebAddress, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, null=False, unique=True)

    def __str__(self):
        return self.text
