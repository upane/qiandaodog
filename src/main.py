import os

from models.v2ex import V2ex
from models.chh import Chh
from models.hifi import Hifini



def main():

    sign_v2ex = V2ex(os.environ["v2ex"])
    sign_v2ex.sign_event()

    sign_chh = Chh(os.environ["chh"])
    sign_chh.sign_event()

    hifini = Hifini(os.environ["hifi"])
    hifini.sign_event()

if __name__ == '__main__':
    main()
