import jpype
import jpype.imports
import os
import yaml
import json

def get_key():
    with open("C:\\Users\\vvvcincn\\PycharmProjects\\SeeKeeAutoApiTest\\config\\config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    readonly_values = {
        key: config["headers"]["common"][key]
        for key in config.get("readonly_keys", [])
    }
    print(readonly_values)
    return readonly_values

keys = get_key()


# 启动 JVM，设置 classpath（可多个jar文件）
jar_files = [
    "C:\\Users\\vvvcincn\\PycharmProjects\\SeeKeeAutoApiTest\\utils\\assets\\SignGenerator-1.0-SNAPSHOT.jar",
    "C:\\Users\\vvvcincn\\PycharmProjects\\SeeKeeAutoApiTest\\utils\\assets\\fastjson-1.2.9.jar",
    # 如果用到了 fastjson 的话
    "C:\\Users\\vvvcincn\\PycharmProjects\\SeeKeeAutoApiTest\\utils\\assets\\slf4j-api-1.7.36.jar",
    "C:\\Users\\vvvcincn\\PycharmProjects\\SeeKeeAutoApiTest\\utils\\assets\\slf4j-simple-1.7.36.jar"
]
jpype.startJVM(
    jpype.getDefaultJVMPath(),
    "--enable-native-access=ALL-UNNAMED",
    classpath=jar_files
)

# 导入 Java 包
from com.loklok import SignGenerator
from com.alibaba.fastjson import JSONObject

class GetAuth:
    def __init__(self, params={},current_time=None):
        self.params = params
        self.current_time = current_time

    def getAuth(self):
        print("getAuth")
        # 准备参数
        #current_time = str(jpype.java.lang.System.currentTimeMillis())
        current_time = self.current_time
        print("current_time:", current_time)
        params = JSONObject()
        print(type(params), params)
        new_params = self.params
        # 手动合并
        for key, value in new_params.items():
            params.put(key, value)
        print("陈睿志",type(params), params)
        public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3bahNR2MaPTf3vCNwORGKjMb+QtvnE58W6PlnXnm8lxYxkpRq4NtcotZm8x5DPnTbfCwrZ0YLh1uOmOCTY+ECYliWT2C6PI0fD8ryleh5+PNmYZVfNq2IVxGIJ+TQ5N2SnpmFgg2TFUg//Cu93GO+0GHJ2B5xzXqi8direBQjZwIDAQAB"

        # 调用 SignGenerator.generate
        res = SignGenerator.generate(params.toJSONString(), current_time)

        # 提取值
        self.sign = str(res.getString("sign"))
        self.encryptAesKey = str(res.getString("encryptAesKey"))
        self.sourceAesKey = str(res.getString("sourceAesKey"))

        print("sign:", self.sign)
        print("aesKey:", self.encryptAesKey)
        print("sourceAesKey:", self.sourceAesKey)



        return  self.sign, self.encryptAesKey


if __name__ == "__main__":
    headers = {
        'User-Agent': 'okhttp/4.10.0',
        'Host': 'test-mobile-api.buscari.com',
        'sysVer': 'android_15_Redmi_AQ3A.240829.003',
        'model': 'zorn_24117RK2CC',
        'netType': '0',
        'zone': 'GMT+08:00',
        'appLanguage': 'zh_CN',
        'mobileId': '7baf80be3202c511',
        'buildCode': '26',
        'channel': 'android_buscari',
        'platformId': '4',
        'system': 'android_15_Redmi_AQ3A.240829.003',
        'deviceModel': 'zorn_24117RK2CC',
        'netStatus': '0',
        'timezone': 'GMT+08:00',
        'lang': 'zh_CN',
        'deviceId': '7baf80be3202c511',
        'versionCode': '26',
        'clientType': 'android_buscari',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'curTime': '1744713245328'
    }
    getAuth = GetAuth(headers=headers)
    getAuth.getAuth()
