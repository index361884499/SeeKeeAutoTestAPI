from math import e
import time
import sys
sys.path.append('.')

from utils.auth import GetAuth
from utils.request_handler import RequestHandler
from utils.yaml_tool import YamlReader


class BuscariAPI:
    def __init__(self, env, channel):
        yaml_reader = YamlReader("config/config.yaml")
        self.request_handler = RequestHandler()
        self.config = yaml_reader.read_yaml()
        self.headers = self.config["headers"]["common"]
        # 这里从配置文件读取登录接口的protocol
        if env == "online":
            protocol = self.config["protocol"]["online"]
        elif env == "test":
            protocol = self.config["protocol"]["test"]
        else:
            raise ValueError(f"{env}没有在yaml中配置")
        # 这里从配置文件读取登录接口的host
        if channel == "ios":
            host = self.config["channel"]["ios"]
        elif channel == "android":
            host = self.config["channel"]["android"]
        else:
            raise ValueError(f"{channel}没有在yaml中配置")
        self.login_url = protocol + host

    def signin(self, email:str,pwd:str):
        """
                邮箱密码登录
        """
        #接口地址：/buscari/user/signin
        #接口方法：POST
        url = self.login_url + "/buscari/user/email/signin"
        print("url:", url)
        #固定参数：signVal、aKey、curTime、token不需要动
        auth = GetAuth()
        headers = self.headers
        headers["curTime"] = str(int(time.time() * 1000))
        print("headers:", headers)
        json = {
            "email": email,
            "password": pwd,
        }
        auth = GetAuth(params=json, current_time=headers["curTime"])
        signVal, aKey = auth.getAuth()
        print(type(signVal), signVal)
        new_headers = {
            "signVal": signVal,
            "aKey": aKey
        }
        headers = {**self.headers, **new_headers}
        print("headers:", headers)
        response = self.request_handler.send_request(method="post", url=url, headers=headers, json=json)
        response = response.json()
        print("邮箱密码登录Resp:", response)
        return response

    def logout(self,token:str):
        """
                        退出登录
        """
        #接口地址：/buscari/user/logout
        #接口方法：GET
        url = self.login_url + "/buscari/user/logout"
        print("url:", url)
        #固定方法
        auth = GetAuth()
        headers = self.headers
        headers["curTime"] = str(int(time.time() * 1000))
        print("headers:", headers)
        #到这都不需要该直接复制，params是请求参数，为空，需要自己修改，直接复制curl到Postman，然后复制里面的params过来
        params = {
          
        }
        auth = GetAuth(params=params, current_time=headers["curTime"])
        signVal, aKey = auth.getAuth()
        print(type(signVal), signVal)
        #检查有没有需要增加的header，有的话就增加，没有就保留signVal、aKey
        new_headers = {
            "signVal": signVal,
            "aKey": aKey,
            "token": token,
            "app_request_proceed_response": "true",
            "sessionId": token
        }
        headers = {**self.headers, **new_headers}
        print("headers:", headers)
        response = self.request_handler.send_request(method="get", url=url, headers=headers, params=params)
        response = response.json()
        print("退出登录resp:", response)
        return response

    def check_registration(self, email:str):
        """
                验证邮箱账号是否注册
        """
        url = self.login_url + "/buscari/user/email/checkRegistration"
        print("url:", url)
        auth = GetAuth()
        headers = self.headers
        headers["curTime"] = str(int(time.time() * 1000))
        print("headers:", headers)
        json = {
            "email": email,
            "type": 0
        }
        auth = GetAuth(params=json, current_time=headers["curTime"])
        signVal, aKey = auth.getAuth()
        print(type(signVal), signVal)
        new_headers = {
            "signVal": signVal,
            "aKey": aKey
        }
        headers = {**self.headers, **new_headers}
        print("headers:", headers)
        response = self.request_handler.send_request(method="post", url=url, headers=headers, json=json)
        response = response.json()
        print("验证邮箱账号是否注册resp:", response)
        return response

    def get_detail(self):
        """
                详情页
        """
        #接口地址：/buscari/user/info/getDetails
        #接口方法：GET
        url = self.login_url + "/buscari/user/info/getDetails"
        print("url:", url)
        #固定方法
        auth = GetAuth()
        headers = self.headers
        headers["curTime"] = str(int(time.time() * 1000))
        print("headers:", headers)
        #到这都不需要该直接复制，params是请求参数，为空，需要自己修改，直接复制curl到Postman，然后复制里面的params过来
        params = {
          
        }
        auth = GetAuth(params=params, current_time=headers["curTime"])
        signVal, aKey = auth.getAuth()
        print(type(signVal), signVal)
        #检查有没有需要增加的header，有的话就增加，没有就保留signVal、aKey
        new_headers = {
            "signVal": signVal,
            "aKey": aKey,
            "token": token,
            "app_request_proceed_response": "true",
            "sessionId": token
        }
        headers = {**self.headers, **new_headers}
        print("headers:", headers)
        response = self.request_handler.send_request(method="get", url=url, headers=headers, params=params)
        response = response.json()
        print("详情页:", response)
        return response


if __name__ == "__main__":  
    email= "361884499@qq.com"
    password= "index361884499"
    app = BuscariAPI(env="test", channel="android")
    app.check_registration(email=email)
    app.signin(email=email,pwd=password)
    app.get_detail()
    app.logout()