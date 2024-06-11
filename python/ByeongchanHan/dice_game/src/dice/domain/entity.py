import random
import uuid
from dataclasses import dataclass, field


class DiceNumber:
    MIN = 1
    MAX = 6


@dataclass
class Dice:
    __id: uuid.UUID = field(init=False)
    dice_number: int = None

    def __post_init__(self):
        self.__id = uuid.uuid4()

    def roll_dice(self):
        self.dice_number = random.randint(DiceNumber.MIN, DiceNumber.MAX)

    @property
    def id(self):
        return self.__id
