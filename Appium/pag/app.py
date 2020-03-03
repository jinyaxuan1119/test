import datetime

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Appium.pag.base_page import BasePage
from Appium.pag.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "6"
            desired_caps["deviceName"] = "emulator-5554"
            desired_caps["automationName"] = "UiAutomator2"
            desired_caps["appPackage"] = self._package
            desired_caps["appActivity"] = self._activity
            #desired_caps["noReset"] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        else:
            self._driver.start_activity(self._package,self._activity)
            self._driver.implicitly_wait(30)
        return self

    def restar(self):
        pass
    def stop(self):
        pass
    def main(self) -> Main:
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source
            if "我的" in source:
                return  True
            if "同意" in source:
                return  True
            return False
        WebDriverWait(self._driver,30).until(wait_load)

        return Main(self._driver);