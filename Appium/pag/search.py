from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Appium.pag.base_page import BasePage


class Search(BasePage):
    _name_locator = (MobileBy.ID, "name")
    def search(self,key:str):
        search = (MobileBy.ID, "search_input_text")
        WebDriverWait(self._driver, 60).until(expected_conditions.visibility_of_element_located(search))
        # self.find(*search).send_keys(key)
        # self.find(self._name_locator).click()
        self.steps("../pag/search.yaml")
        return self
        #todo:业务输入

    def get_price(self,key:str) -> float:
        price_search = (MobileBy.XPATH,'//*[@text="%s"]'%key)
        WebDriverWait(self._driver,30).until(expected_conditions.visibility_of_element_located(price_search))
        return float(self.find(MobileBy.ID,"current_price").text)




