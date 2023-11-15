import os

from models.v2ex import V2ex
from models.chh import Chh

if __name__ == '__main__':
    # v2ex_cookie = sys.argv[1]
    # chh_cookie = sys.argv[2]

    v2ex_cookie = os.environ["v2ex"]
    chh_cookie = os.environ["chh"]

    sign_v2ex = V2ex(v2ex_cookie)
    sign_v2ex.sign_event()

    sign_chh = Chh(chh_cookie)
    sign_chh.sign_event()

