from time import sleep
from appium import webdriver
import unittest

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy


class TestXueQiu(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "9"
        desired_caps["deviceName"] = "93879e1f"
        desired_caps["automationName"] = "UiAutomator2"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["noReset"] = True


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        sleep(10)

    # def test_one(self):
    #     self.driver.find_element(MobileBy.ID,"home_search").click()
    #     self.driver.find_element(MobileBy.ID,"search_input_text").send_keys("阿里巴巴")
    #     self.driver.find_element(MobileBy.ID,"name").click()
    #     sleep(5)
    #     assert float(self.driver.find_element(MobileBy.ID,"current_price").text) > 200


    def test_two(self):
        self.driver.find_element(MobileBy.ID, "home_search").click()
        sleep(3)
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        sleep(8)
        self.driver.find_element(MobileBy.ID, "name").click()
        sleep(5)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="股票"]').click()
        print(self.driver.page_source)
        float(self.driver.find_element(MobileBy.XPATH, '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]').text) > 200
        #gupiao = self.driver.find_element(MobileBy.XPATH, '//*[contains(@resource-id,"current_price")]/../../.. //*[@text="09988"]').text
        #self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!")#MobileBy.ACCESSIBILITY_ID专门用户获取content-desc属性信息

    def test_three(self):
        self.driver.find_element(MobileBy.ID, "home_search").click()
        sleep(3)
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        sleep(8)
        self.driver.find_element(MobileBy.ID, "name").click()
        sleep(5)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="股票"]').click()
        #点击已添加
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id,"follow_btn")]').click()

        #点击取消
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@resource-id,"action_close") and //*[@text="取消"]]').click()

        #重新选择
        self.driver.find_element(MobileBy.ID, "home_search").click()
        sleep(3)
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        sleep(8)
        self.driver.find_element(MobileBy.ID, "name").click()
        sleep(5)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="股票"]').click()

        #获取已添加控件信息
        neirong = self.driver.find_element(MobileBy.XPATH,
                                 '//*[@text="09988"]/../../..//*[contains(@resource-id,"followed_btn")]').get_attribute("name")
        # neirong = self.driver.find_element(MobileBy.XPATH,
        #                                    # '//*[@text="09988"]/../../..//*[contains(@resource-id,"followed_btn")]').text
        #判断内容是否为 已添加
        assert neirong == "已添加"

    def test_four(self):
        #获取屏幕大小，进行滑动
        size = self.driver.get_window_size()
        TouchAction(self.driver) \
            .long_press(x=size['width']*0.5,y=size['height']*0.8) \
            .move_to(x=size['width']*0.5,y=size['height']*0.2) \
            .release() \
            .perform()

    def test_gunping(self):
        #捕获文本信息进行滑动，直到找到文本位置
        scroll_to_element = (
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
                'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()


    def tearDown(self):
        sleep(10)
        #self.driver.quit()


if __name__ == "__main__":
    unittest.main()