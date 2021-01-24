import json
from unittest.mock import MagicMock

import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

# from simple_rest_api.scrap_app.views import WebAddressViewSet
from .data_fixtures import api_client, create_default_web_address


@pytest.mark.django_db
def test_webs_list_method_get(api_client, create_default_web_address):
    # given
    create_default_web_address()
    url = reverse('scrap_app:webaddress-list')
    # when
    response = api_client.get(url)
    # then
    content = json.loads(response.content)
    assert response.status_code == HTTP_200_OK
    assert len(content['results']) == 1
    assert content['count'] == len(content['results'])


@pytest.mark.django_db
def test_webs_list_method_post(api_client, create_default_web_address, mocker):
    # given
    mock: MagicMock = mocker.patch('os.system')
    mock.return_value = 0
    web = create_default_web_address()
    url = reverse('scrap_app:webaddress-list')
    link = web.link
    data = {
        'link': link,
    }
    # when
    response = api_client.post(
        path=url,
        data=json.dumps(data),
        content_type='application/json'
    )
    # then
    content = json.loads(response.content)
    assert response.status_code == HTTP_201_CREATED
    assert content['uuid'] is not None
    assert content['link'] == link


@pytest.mark.django_db
def test_webs_list_method_should_fail(api_client):
    # given
    url = reverse('scrap_app:webaddress-list')
    link = 'wp.pl'
    data = {
        'link': link,
    }
    # when
    response = api_client.post(
        path=url,
        data=json.dumps(data),
        content_type='application/json'
    )
    # then
    content = json.loads(response.content)
    assert response.status_code == HTTP_400_BAD_REQUEST

