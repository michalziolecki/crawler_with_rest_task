import pytest
from pytest_mock import MockerFixture
from unittest.mock import MagicMock

from rest_framework.status import HTTP_200_OK, HTTP_307_TEMPORARY_REDIRECT, HTTP_404_NOT_FOUND

from scraper_src.request_controller import RequestController
from scraper_src.text_scraper import TextScraper
from requests.models import Response
from .data_fixtures import create_default_web_address
from data.utils import include_django_orm

include_django_orm()
from data.models import TextData


def test_request_controler_bad_link_should_fail():
    # given
    controller = RequestController()
    find_text = True
    find_img = True
    # when
    result = controller.run_request('onet.pl', find_text, find_img)
    # then
    assert result == HTTP_404_NOT_FOUND


def test_request_controler_bad_response_should_fail(requests_mock):
    # given
    controller = RequestController()
    find_text = True
    find_img = True
    url = 'https://onet.pl'
    requests_mock.get(url, status_code=307)
    # when
    result = controller.run_request(url, find_text, find_img)
    # then
    assert result == HTTP_307_TEMPORARY_REDIRECT


@pytest.mark.django_db
def test_prepare_text_and_save_in_db(create_default_web_address):
    # given
    web_entity = create_default_web_address()
    text = """
        aaa
        bbb
        ccc
    """
    # when
    TextScraper.prepare_text_and_save_in_db(text, web_entity)
    texts = TextData.objects.all()
    assert len(texts) == 3
