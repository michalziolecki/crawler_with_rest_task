import requests
from requests.models import Response
from multiprocessing import Process, Lock
import copy

from django.utils import timezone
from scraper_src.img_scraper import ImageScraper
from scraper_src.text_scraper import TextScraper
from rest_framework.status import HTTP_200_OK, HTTP_300_MULTIPLE_CHOICES
from data.utils import include_django_orm
include_django_orm()

from data.models import WebAddress, TextData, ImageData


class RequestController:

    def __init__(self):
        self.img_locker = Lock()
        self.text_locker = Lock()
        self.img_scraper = ImageScraper(self.img_locker)
        self.text_scraper = TextScraper(self.text_locker)

    def run_request(self, url: str, find_text: bool, find_img: bool) -> int:
        response: Response = requests.get(url)

        if response.status_code < HTTP_200_OK or response.status_code >= HTTP_300_MULTIPLE_CHOICES:
            return response.status_code

        web = None
        if WebAddress.objects.filter(link=url).exists():
            web = WebAddress.objects.filter(link=url).get()
            if web.validity_term < timezone.now():
                web.delete()  # delete cascade all connected to this link data
                web = WebAddress(link=url)
                web.save()
        else:
            web = WebAddress(link=url)
            web.save()

        if web:
            text_lookup: bool = TextData.objects.filter(related_web_addr=web).count() == 0
            img_lookup: bool = ImageData.objects.filter(related_web_addr=web).count() == 0
            find_text = find_text and text_lookup
            find_img = find_img and img_lookup
            self.run_processes(response.content, find_text, find_img, web)
        return response.status_code

    def run_processes(self, content, find_text: bool, find_img: bool, web):
        content_copy = copy.deepcopy(content)
        t_scraper_proccess = Process(target=self.text_scraper.run_scraping, args=(content, web))
        i_scraper_proccess = Process(target=self.img_scraper.run_scraping, args=(content_copy, web))
        if find_text:
            t_scraper_proccess.start()
        if find_img:
            i_scraper_proccess.start()
        if t_scraper_proccess.is_alive():
            t_scraper_proccess.join()
        if i_scraper_proccess.is_alive():
            i_scraper_proccess.join()
