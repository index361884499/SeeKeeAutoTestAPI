import time

import requests
import logging



formatted_time = time.time()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=f'C:\\Users\\vvvcincn\\PycharmProjects\\SeeKeeAutoApiTest\\logs\\{formatted_time}.log')

class RequestHandler:
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, headers=None, params=None, json=None, auth=None):
        valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
        method = method.upper()
        if method not in valid_methods:
            logging.error(f"无效的请求方法: {method}。支持的方法有: {', '.join(valid_methods)}")
            return None

        try:
            logging.info(f"发送 {method} 请求到 {url}")
            logging.info(f"请求头: {headers}")
            logging.info(f"请求参数: {params}")
            logging.info(f"请求体: {json}")

            response = self.session.request(method, url, headers=headers, params=params, json=json, auth=auth)

            logging.info(f"响应状态码: {response.status_code}")
            try:
                logging.info(f"响应内容: {response.json()}")
            except ValueError:
                logging.info(f"响应内容: {response.text}")

            return response
        except requests.RequestException as e:
            logging.error(f"请求出错: {e}")
            return None