import pytest

from Appium.pag.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_search_page_().search("alibaba").get_price("BABA") > 200

    @pytest.mark.parametrize("key,stock_type,pirce",[
        ("alibaba","BABA",200),
        ("JD","JD",20)
    ])
    def test_search(self,key,stock_type,pirce):
        assert self.main.goto_search_page_().search("key").get_price("stock_type") > pirce