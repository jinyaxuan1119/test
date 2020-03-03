from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging

class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver:WebDriver
    _black_list = [
        (By.ID,"tv_agree"),
        (By.XPATH, '//*[@text = "确定"]'),
    ]
    _error_max = 10
    _error_count = 0
    def __init__(self,driver:WebDriver = None):
        self._driver = driver

    def find(self,locator,value=None):
        logging.info(locator)
        logging.info(value)

        try:
            if isinstance(locator,tuple):
                self._error_count = 0
                return self._driver.find_element(*locator)
            else:
                self._error_count = 0
                return self._driver.find_element(locator,value)
        except Exception as e:
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(locator,value)
            logging.warn("black list no one found")
            raise e
