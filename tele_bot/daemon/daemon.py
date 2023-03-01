import os
from time import sleep
from tele_bot.settings import conf
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from bs4 import BeautifulSoup as Bs
from tele_bot.daemon.path import ButtonXpath, FilePath


class Driver:
    def __init__(self, url):
        self.url = url
        self.options = Options()
        self.options.add_argument(f"user_agent={conf.user_agent}")
        self.options.add_argument("--disable-blink-features=AutomationContrilled")
        self.options.add_argument("--headless")
        self.servis = Service(conf.BASE_DIR / "daemon" / "driver" / "chromedriver")
        self.pause = 3

    def aktivation(self):
        self.driver = webdriver.Chrome(service=self.servis, options=self.options)
        self.driver.implicitly_wait(60)
        self.driver.set_window_size(1920, 1080)

    def get(self):
        self.driver.get(self.url)
        sleep(self.pause)

    def save(self, file_name):
        page = Bs(self.driver.page_source, features="lxml")
        container = page.select_one("#singlePage > div > div.row.b-shdow.grey-bg")
        if os.path.exists(file_name.parent):
            with open(file_name, "w") as file:
                file.write(str(container))
        else:
            os.mkdir(file_name.parent)
            with open(file_name, "w") as file:
                file.write(str(container))

    def ending(self):
        self.driver.close()
        self.driver.quit()

    def get_data_checkpoint(self):
        for file_path in FilePath:
            self.driver.find_element(
                by=By.XPATH, value=file_path.value["xpath"]
            ).click()
            sleep(self.pause)
            self.save(file_path.value["cargo_path"])
            self.driver.find_element(
                by=By.XPATH, value=ButtonXpath.BUTTON.value
            ).click()
            self.driver.find_element(
                by=By.XPATH, value=ButtonXpath.BUTTON_PASSENGER.value
            ).click()
            self.save(file_path.value["passenger_path"])
            self.driver.find_element(
                by=By.XPATH, value=ButtonXpath.BUTTON.value
            ).click()
            self.driver.find_element(
                by=By.XPATH, value=ButtonXpath.BUTTON_BUS.value
            ).click()
            self.save(file_path.value["bus_path"])
            self.driver.find_element(by=By.XPATH, value=ButtonXpath.BACK.value).click()


def run_daemon():
    browser = Driver("https://mon.declarant.by/zone")
    browser.aktivation()
    try:
        browser.get()
        browser.get_data_checkpoint()
    except (NoSuchElementException, ElementNotInteractableException):
        browser.ending()


if __name__ == "__main__":
    run_daemon()
