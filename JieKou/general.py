import requests


class General:
    # 此处方法尽量简单，数据整理均之前进行处理
    #固定内容，不考虑传参
    url_token = ' https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'wwf803852289492aef'

    def general_get_token(self, corpsecret):
        #通用获取token方式，返回token
        r = requests.get(url=self.url_token, params={"corpid": self.corpid, "corpsecret": corpsecret})
        return r.json()['access_token']

    def request_get(self,url,id):
        #get方法地址变动，通过传参获取
        #此处关键参数只针对通讯录，后续其它扩容在调整
        r = requests.get(url, params={"access_token": self.token, "id": id})
        return r.json()


    def request_post(self,url,token,body):
        # POST方法地址变动，通过传参获取
        # 此处关键参数只针对通讯录，后续其它扩容在调整
        r = requests.post(url, params={"access_token": token}, json=body)
        return r.json()
