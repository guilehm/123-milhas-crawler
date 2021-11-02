import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from driver.driver_builder import Driver

BASE_URL = 'https://123milhas.com/'


class FlightsCrawler:
    def __init__(self, headless=True, url=BASE_URL):
        self.url = url
        self.driver = Driver(headless=headless).get_driver()
        self._get_page()

    def _get_page(self):
        self.driver.get(self.url)

    def set_departure_and_arrival(self, departure_airport, arrival_airport):
        for input_id, airport in [
            ('txtDepartureLocation', departure_airport),
            ('txtArrivalLocation', arrival_airport),
        ]:

            element = self.driver.find_element(
                By.XPATH,
                f'//input[@id="{input_id}"]',
            )
            element.send_keys(airport)
            time.sleep(1)
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

    def set_outbound_mont_and_year(self, text):
        time.sleep(1)
        try:
            self.driver.find_element(
                By.XPATH,
                f'//button[contains(string(), "{text}")]',
            )
            self.click_next_month()
        except NoSuchElementException:
            self.click_next_month()
            self.set_outbound_mont_and_year(text)

    def set_outbound_day(self, day):
        self.driver.find_element(
            By.XPATH,
            f'//tr[@class="uib-weeks"]/td[@class="uib-day text-center"]/button[contains(string(), "{day}")]'
        ).click()

    def search(self):
        self.driver.find_element(
            By.XPATH,
            '//button[@id="buttonSearch"]'
        ).click()


c = FlightsCrawler(headless=False)

# c.set_departure()

# c.set_arrival()
c.set_departure_and_arrival('congonhas', 'Nova Iorque - Todos')
c.click_outbound_input()
c.set_outbound_mont_and_year('julho de 2022')

c.set_outbound_day('01')
time.sleep(1)
c.search()
