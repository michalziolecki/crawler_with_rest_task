import datetime

import requests
from requests.models import Response
from multiprocessing import Process, Lock
import copy
from scraper_src.img_scraper import ImageScraper
from scraper_src.text_scraper import TextScraper


class RequestController:

    def __init__(self):
        self.img_locker = Lock()
        self.text_locker = Lock()
        self.img_scraper = ImageScraper(self.img_locker)
        self.text_scraper = TextScraper(self.text_locker)

    def run_request(self, url: str, find_text: bool, find_img: bool) -> int:
        response: Response = requests.get(url)
        content_copy = copy.deepcopy(response.content)
        test = datetime.datetime.now()
        # self.img_scraper.run_scraping(content=response.content)
        # self.text_scraper.run_scraping(content=response.content)
        # print(response.text)
        t_scraper_proccess = Process(target=self.text_scraper.run_scraping, args=(response.content,))
        i_scraper_proccess = Process(target=self.img_scraper.run_scraping, args=(content_copy,))
        if find_text:
            t_scraper_proccess.start()
        if find_img:
            i_scraper_proccess.start()
        if t_scraper_proccess.is_alive():
            t_scraper_proccess.join()
        if i_scraper_proccess.is_alive():
            i_scraper_proccess.join()
        print(f'test={datetime.datetime.now() - test}')
        return response.status_code
