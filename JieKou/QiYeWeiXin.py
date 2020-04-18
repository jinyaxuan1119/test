import requests

from JieKou.general import General


class QiYeWiXin(General):
    #此类只针对通讯录（增删改查），其它功能单独创建测试类
    #主要用于中间过程以及处理数据
    #尽量调整通用方法的修改
    #传参规则按照General类方法调整
    token= None
    def get_token(self,corpsecret):
        #用于获取本应用touken
        r = QiYeWiXin.general_get_token(self,corpsecret)
        self.token = r


    def create_department(self,name,id,**kwargs):
        create = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        body = {
            'name':name,
            'parentid':id
        }
        body.update(kwargs)
        r = QiYeWiXin.request_post(self,create,body=body,token=self.token)
        return r

    def update_create_department(self,name,id,**kwargs):
        update_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        body = {
            'name': name,
            'id': id
        }
        body.update(kwargs)
        r = QiYeWiXin.request_post(self,update_url,body=body,token=self.token)
        return r

    def select_department(self,id):
        select_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r = QiYeWiXin.request_get(self,url=select_url,id=id)
        return r

    def delete_department(self,id):
        delete_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r = QiYeWiXin.request_get(self,url=delete_url,id=id)
        return r
