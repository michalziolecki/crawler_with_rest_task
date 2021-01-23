from multiprocessing import Lock

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import Response
from rest_framework.status import HTTP_200_OK

from scraper_src.abstract_scraper import AbstractScraper
from data.utils import include_django_orm

include_django_orm()
from data.models import ImageData


class ImageScraper(AbstractScraper):

    def __init__(self, locker: Lock):
        super().__init__(locker)

    def run_scraping(self, content, web_entity):
        soup = BeautifulSoup(content, 'html.parser')
        images = soup.find_all('img')
        ImageScraper.prepare_linked_images(images, web_entity)

    @staticmethod
    def prepare_linked_images(images, web_entity):

        def check_source(link: str, prefix='') -> tuple:
            link = f'{prefix}{link}'
            response: Response = requests.get(link)
            content_type: str = response.headers.get('Content-Type')
            if response.status_code == HTTP_200_OK and 'image' in content_type:
                return True, link
            return False, link

        for image in images:
            image: Tag
            alt = image.get('alt')
            src = image.get('src')
            correct_source = False
            if src and src.startswith('//'):
                correct_source, src = check_source(src, 'https:')
                if not correct_source:
                    correct_source, src = check_source(src, 'http:')
            elif src.startswith('http'):
                correct_source, src = check_source(src)
            else:
                correct_source, src = check_source(src, 'https://')
                if not correct_source:
                    correct_source, src = check_source(src, 'http://')
            if correct_source:
                img_entity = ImageData(related_web_addr=web_entity, alt=alt, src=src)
                img_entity.save()
