from appium import webdriver

from Appium.demo import zhuye
from Appium.demo.hexin import HeXin
from Appium.demo.zhuye import Zhuye


class PeiZhi(HeXin):
    appname = "com.xueqiu.android"
    appactivity = '.view.WelcomeActivityAlias'
    def kaishi(self):
        info = {}
        info['platfromName'] = "Android"
        info['platfromVersion'] = "9"
        info['deviceName'] = "93879e1f"
        info['appPackage'] = "appname"
        info['appActivity'] = "appactivity"
        # info["noReset"] = True

        self._driver = webdriver.Remote("http://localhost:4723/wd/hub",info)
        return self

    def zhuye(self) -> zhuye:
        return Zhuye(self._driver)
