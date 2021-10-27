from driver.driver_builder import Driver
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://123milhas.com/'


class FlightsCrawler:
    def __init__(self, headless=True, url=BASE_URL):
        self.url = url
        self.driver = Driver(headless=headless).get_driver()

    def _get_page(self):
        self.driver.get(self.url)