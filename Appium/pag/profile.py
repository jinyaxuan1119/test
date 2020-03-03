from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Appium.pag.base_page import BasePage


class Profile(BasePage):
    def login_by_password(self,phone,password):

       # mima = (By.XPATH,"//*[@text='帐号密码登录']")
        #WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@text='帐号密码登录']")))
        self.find(By.XPATH, "//*[@text='帐号密码登录']").click()
        #WebDriverWait(self._driver,30).until(expected_conditions.visibility_of_element_located((By.ID, "login_account")))
        self.find(By.ID, "login_account").send_keys(phone)
        self.find(By.ID, "login_password").send_keys(password)

       # WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "button_next")))
        self.find(By.ID, "button_next").click()

        #WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of_element_located((By.ID, "md_content")))
        msg = self.find(By.ID, "md_content").text
        self.find(By.ID, "md_buttonDefaultPositive").click()
        return msg