from abc import ABC, abstractmethod


class AccountRepository(ABC):

    @abstractmethod
    def method(self):
        pass