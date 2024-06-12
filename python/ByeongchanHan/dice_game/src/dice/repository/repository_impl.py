from src.dice.domain import Dice

from .repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__dice_list = []

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def roll_dice(self):
        dice = Dice()
        dice.roll_dice()
        self.__dice_list.append(dice)

    @property
    def dice_list(self):
        return self.__dice_list
