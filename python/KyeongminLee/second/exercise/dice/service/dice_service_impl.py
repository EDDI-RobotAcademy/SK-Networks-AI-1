from dice.entity.dice import Dice
from dice.service.dice_service import DiceService
from dice.repository.dice_repository_impl import DiceRepositoryImpl
import random


# 파이썬 상속은 아래와 같이 class A(상속할 클래스) 형태로 상속을 진행
class DiceServiceImpl(DiceService):
    # Singleton(싱글톤) 객체를 만들기 위한 기법 시작
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    # Singleton(싱글톤) 객체를 만들기 위한 기법 끝
    def rollDice(self):
        self.__diceRepository.rollDice()


    def getDiceList(self):
        return self.__diceRepository.getDiceList()

