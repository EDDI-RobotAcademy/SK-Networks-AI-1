from dice_game.dice.repository.dice_repository_impl import DiceRepositoryImpl
from dice_game.dice.service.dice_service import DiceService


class DiceServiceImpl(DiceService):
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

    def rollDice(self):
        self.__diceRepository.rollDice()

    def getDiceList(self):
        return self.__diceRepository.getDiceList()
