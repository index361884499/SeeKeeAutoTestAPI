import sys
sys.path.append('.')
from api.buscari_api.buscari_api import BuscariAPI

class App:
    def __init__(self, env, channel, email, pwd):
        self.buscari = BuscariAPI(env, channel)
        self.email = email
        self.pwd = pwd
        self.token = None


    def signin(self):
        resp = self.buscari.signin(self.email, self.pwd)
        if resp["msg"] != "Success":
            return resp
        else:
            token = resp["data"]["userInfoBaseResp"]["token"]
            self.token = token
            return resp
        

    def logout(self):
        resp = self.buscari.logout(token=self.token)
        return resp

    def check_registration(self,email:str= None):
        if email is None:
            email = self.email
        resp = self.buscari.check_registration(email=email)
        return resp

    def get_detail(self):
        resp = self.buscari.get_detail(token=self.token)
        return resp

if __name__ == "__main__":
    app = App("test", "android", "361884499@qq.com", "index3618844991")
    resp = app.signin()
    resp = app.logout()
    resp = app.check_registration()  # 这里会报错，因为token是None，无法进行logout操作，需要先调用signin方法获取token后才能调用logout方法，否则会报错
    print(resp)
