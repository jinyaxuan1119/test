from time import sleep
from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu:
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6"
        desired_caps["deviceName"] = "emulator-5554"
        desired_caps["automationName"] = "UiAutomator2"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["noReset"] = True
        #chromedriver自适应查找
        #desired_caps["chromedriverExecutableDir"]="D:\chromedriver"
        #指定使用哪个版本
        desired_caps["chromedriverExecutable"] = "D://chromedriver/chromedriver--2.20.43.exe"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        sleep(20)

    def test_webview_debug(self):
        self.driver.find_element(By.XPATH,"//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        #获取上下文
        for i in range(5):
            print(self.driver.contexts)
            sleep(1)
        #print(self.driver.page_source)
        WebDriverWait(self.driver,30).until(lambda x:(self.driver.contexts) > 1)
        #切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        #print(self.driver.page_source)

        print(self.driver.window_handles)#获取当前的窗口数量,返回一个列表
        self.driver.find_element(By.CSS_SELECTOR,".trade_home_info_3aI").click()
        for i in range(5):
            print(self.driver.window_handles)
            sleep(1)
        #切换窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.ID,"phone-number")
        WebDriverWait(self.driver,30).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys("13811263249")

    def tearDown(self):
        pass