import time

from utils.auth import GetAuth
from utils.request_handler import RequestHandler
from utils.yaml_tool import YamlReader
from common.app import App


class ContentRecommentApi:
    def __init__(self,env,channel):
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

    def content_recommend_discover(self):
        """
        搜索页历史搜索结果
        """
        url = self.login_url + "/quan/app/content/recommend/discover"
        print("url:",url)
        auth = GetAuth()
        headers = self.headers
        headers["curTime"] = str(int(time.time()*1000))
        print("headers:", headers)
        params = {

        }
        auth = GetAuth(params=params,current_time=headers["curTime"])
        signVal,aKey = auth.getAuth()
        print(type(signVal), signVal)
        new_headers = {
            "signVal": signVal,
            "aKey": aKey
        }
        headers = {**self.headers, **new_headers}
        print("headers:", headers)
        response = self.request_handler.send_request(method="get", url=url, headers=headers, params=params)
        response= response.json()
        print("response:", response)
        return response

if __name__ == "__main__":
    ContentRecommentApi(env="test", channel="android").content_recommend_discover()