from selenium.webdriver.common.by import By

from Appium.demo.hexin import HeXin


class Zhuye(HeXin):
    def click_sousuo(self):
       return self._driver.find_element(By.ID,"")