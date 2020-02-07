from abc import ABC, abstractmethod


class AbstractRequestFactory(ABC):

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def create_post(self):
        pass

    @abstractmethod
    def create_token(self):
        pass


class RequestBodyFactory(AbstractRequestFactory):
    pass
