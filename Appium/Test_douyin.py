from appium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDouyin():
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "9"
        desired_caps["deviceName"] = "93879e1f"
        desired_caps["automationName"] = "UiAutomator2"
        desired_caps["appPackage"] = "com.ss.android.ugc.aweme"
        desired_caps["appActivity"] = ".splash.SplashActivity"
        desired_caps["noReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        sleep(10)

    def test_zhuye(self):
        phone = (By.XPATH,"//*[@text='我的']")
        WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(phone))
    

