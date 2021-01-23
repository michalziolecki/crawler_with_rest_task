import pytest
import uuid
from django.utils import timezone

from data.utils import include_django_orm

include_django_orm()
from data.models import ImageData, TextData, WebAddress
from .data_fixtures import create_default_web_address


@pytest.mark.django_db
def test_create_web_address():
    # given
    web = WebAddress(link='test_link')
    # when
    web.save()
    # then
    webs = WebAddress.objects.all()
    assert len(webs) == 1
    assert webs[0].link == web.link
    assert webs[0].uuid == web.uuid
    assert webs[0].validity_term > timezone.now()
    assert isinstance(webs[0].uuid, uuid.UUID)


@pytest.mark.django_db
def test_create_text_data(create_default_web_address):
    # given
    web = create_default_web_address()
    text_entity = TextData(text='test_text', related_web_addr=web)
    # when
    text_entity.save()
    # then
    texts = TextData.objects.all()
    assert len(texts) == 1
    assert texts[0].text == text_entity.text
    assert texts[0].uuid == text_entity.uuid
    assert isinstance(texts[0].uuid, uuid.UUID)


@pytest.mark.django_db
def test_create_image_data(create_default_web_address):
    # given
    web = create_default_web_address()
    image_entity = ImageData(alt='test_alt', src='http://abc.com', related_web_addr=web)
    # when
    image_entity.save()
    # then
    images = ImageData.objects.all()
    assert len(images) == 1
    assert images[0].alt == image_entity.alt
    assert images[0].src == image_entity.src
    assert images[0].uuid == image_entity.uuid
    assert isinstance(images[0].uuid, uuid.UUID)
