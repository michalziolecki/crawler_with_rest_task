import pytest
from rest_framework.test import APIClient

from ..models import WebAddress


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_default_web_address():
    def inner():
        web = WebAddress(link='http://wp.pl')
        web.save()
        return web

    return inner
