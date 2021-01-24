import pytest

from ..models import WebAddress


@pytest.fixture
def create_default_web_address():
    def inner():
        web = WebAddress(link='test_link')
        web.save()
        return web

    return inner
