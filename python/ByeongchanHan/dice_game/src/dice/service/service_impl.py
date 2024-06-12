from src.dice.repository.repository_impl import DiceRepositoryImpl

from .service import DiceService


class DiceServiceImpl(DiceService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__dice_repository = DiceRepositoryImpl.get_instance()

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def roll_dice(self):
        self.__dice_repository.roll_dice()

    @property
    def dice_list(self):
        return self.__dice_repository.dice_list
