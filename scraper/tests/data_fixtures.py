import pytest
from data.utils import include_django_orm

include_django_orm()
from data.models import WebAddress


@pytest.fixture
def create_default_web_address():
    def inner():
        web = WebAddress(link='test_link')
        web.save()
        return web

    return inner
