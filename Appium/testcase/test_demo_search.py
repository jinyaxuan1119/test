from Appium.demo.peizhi import PeiZhi


class TestSearch:
    def setup(self):
        self.zhuye =  PeiZhi().kaishi().zhuye()

    def test_zhuye_dianji(self):
        self.zhuye.click_sousuo().click()