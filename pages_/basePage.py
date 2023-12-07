from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_.utilities_.customLogger import *


class BasePage():
    def _init_(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
        except:
            logger("Error: Element not Found")
            return element
            exit(1)

    def _click(self, webElement):
        webElement.click()

    def _fill_field(self, webElement, text):
        webElement.clear()
        webElement.send_keys(text)

    def _get_title(self):
        logger("INFO", f"The title is found successfully: {self.driver.title}")
        return self.driver.title

    def _get_element_text(self, webElement):
        logger("INFO", f"Text is founded: {webElement.text}")
        return self.element.text
