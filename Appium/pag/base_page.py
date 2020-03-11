import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging

class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver:WebDriver
    _black_list = [
        (By.ID,"tv_agree"),
        (By.XPATH, '//*[@text = "确定"]'),
        (By.XPATH, '//*[@text = "同意"]'),
    ]
    #_error_max = 10
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
            if self._error_count > len(self._black_list):
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

    def get_toast(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        return self.find(self.text(key))

    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            content = content.replace("{%s}" % key, self._params[key])
                        element.send_keys(content)