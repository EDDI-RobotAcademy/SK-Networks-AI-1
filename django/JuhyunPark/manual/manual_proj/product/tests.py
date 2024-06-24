from django.test import TestCase
from abc import ABC, abstractmethod
# Create your tests here.

class CartService(ABC):
    @abstractmethod
    def cartRegister(self, cartData, accountId):
        pass


