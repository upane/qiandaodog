from abc import ABC, abstractmethod

class BaseSigner(ABC):

    # Abstract Base Classes (ABCs)
    def __init__(self, cookies):
        self.cookies = cookies

    @abstractmethod
    def sign_event(self):
        pass