from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Appium.pag.base_page import BasePage
from Appium.pag.profile import Profile
from Appium.pag.search import Search


class Main(BasePage):
    def goto_search_page(self):
        search = (MobileBy.ID, "home_search")
        WebDriverWait(self._driver,60).until(expected_conditions.visibility_of_element_located(search))
        self.find(*search).click()
        return Search(self._driver)
    def goto_stocks(self):
        pass
    def goto_trade(self):
        pass
    def goto_profile(self):
        wode = (By.XPATH,"//*[@text='我的']")
        WebDriverWait(self._driver, 60).until(expected_conditions.visibility_of_element_located(wode))
        self.find(By.XPATH,"//*[@text='我的']").click()
        return Profile(self._driver)
    def goto_messages(self):
        pass