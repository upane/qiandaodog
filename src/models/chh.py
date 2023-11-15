import requests

class Chh:
    def __init__(self, cookies):
        self.cookies = cookies
        self.url = ""

    def sign_event(self):
        self.url = "https://www.chiphell.com/"
        try:
            self.get_chh()
            print("CHH 已发送签到请求")
        except Exception as e:
            print("CHH 站点打开失败")
            print(e)

    def get_chh(self):
        headers = {
            "Cookie": self.cookies,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()

