# @author Dragon_qing
# encoding utf-8
import random
import time

import requests

from models.BaseSigner import BaseSigner


class Hifini(BaseSigner):

    SIGN_IN_URL = "https://www.hifini.com/sg_sign.htm"
    TEST_URL = "http://httpbin.org/get"

    def sign_event(self):
        headers = {
            "origin": "https://www.hifini.com",
            "referer": "https://www.hifini.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "accept": "text/plain, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9"
        }
        for i in range(1):
            try:
                response = requests.post(url=self.SIGN_IN_URL, headers=headers, cookies=self.cookies,  verify=False)
                print(response.json()["message"])
            except Exception as e:
                print(e)
                time.sleep(0.3*random.random())

        # with open("hifini.html", "wb") as f:
        #     f.write(response.content)
