import requests
import re

class V2ex:
    def __init__(self, cookies):
        self.cookies = cookies
        self.url = ""
        self.html_body = ""

    def sign_event(self):
        self.url = "https://www.v2ex.com/mission/daily"
        try:
            self.get_v2ex()
        except Exception as e:
            print("打开V2EX失败!")
            return

        html = re.search(r'(<input type="button" class="super normal button" value="领取 X 铜币" onclick="location.href = \'[^\']+|每日登录奖励已领取)', self.html_body)
        if html.group() == '每日登录奖励已领取':
            print("V2ex 每日登录奖励已领取过")
        elif not html:
            print("V2EX 未登录")
        else:
            self.url = "https://www.v2ex.com" + re.search(r'[^\'$]+$', html.group()).group()
            try:
                self.get_v2ex()
            except Exception as e:
                print("V2EX 签到失败")
                return
            print("V2EX 签到成功")

    def get_v2ex(self):
        headers = {
            "Cookie": self.cookies,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }
        try:
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            self.html_body = response.text
        except Exception as e:
            raise e





