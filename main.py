from selenium.common.exceptions import NoSuchElementException

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

    def set_departure(self, airport='congonhas'):
        departure_input = self.driver.find_element(
            By.XPATH,
            '//input[@id="txtDepartureLocation"]',
        )
        departure_input.send_keys(airport)
        time.sleep(1)
        # click on first result
        self.driver.find_element(
            By.XPATH,
            '//ul[@class="dropdown-menu"]/li/a[@class="airport"]',
        ).click()

    def set_arrival(self, airport='Nova Iorque - Todos'):
        arrival_input = self.driver.find_element(
            By.XPATH,
            '//input[@id="txtArrivalLocation"]',
        )
        arrival_input.send_keys(airport)
        time.sleep(1)
        # click on first result
        self.driver.find_element(
            By.XPATH,
            '//ul[@class="dropdown-menu"]/li/a[@class="airport"]',
        ).click()

    def click_next_month(self):
        self.driver.find_element(
            By.XPATH,
            '//table[@class="uib-daypicker"]//tr[@class="uib-monthname"]//button[contains(@class, "pull-right")]',
        ).click()

    def click_outbound_input(self):
        self.driver.find_element(
            By.XPATH,
            '//input[@id="txtOutboundDate"]',
        ).click()