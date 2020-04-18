import requests

from JieKou.QiYeWeiXin import QiYeWiXin


class Test_cases:
    weixin = QiYeWiXin()
    secret = 'NguueWMLcu_UfTWMtyICJAQG0v_MQ8xJeT-TZx64oPY'
    def setup(self):
        self.weixin.get_token(self.secret)

    def test_create(self):
        name = "测试开发"
        id = 1
        r = self.weixin.create_department(name=name,id=id)
        assert r["errmsg"] == "created"


    def test_update(self):
        name = "完美世界测试开发"
        id =2
        r = self.weixin.update_create_department(name=name, id=id)
        assert r["errmsg"] == "updated"

    def test_select(self):
        id = 2
        r = self.weixin.select_department(id=id)
        assert r["errmsg"]== "ok"


    def test_delete(self):
        id = 2
        r = self.weixin.delete_department(id=id)
        assert r["errmsg"] == "deleted"