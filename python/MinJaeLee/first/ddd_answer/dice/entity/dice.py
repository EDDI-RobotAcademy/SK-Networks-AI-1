from random import random

from first.ddd_answer.dice.entity.DiceNumber import DiceNumber


class Dice:
    # __ 는 접근제한자의 역할로 private를 의미합니다.
    # 그러므로 외부에서 __가 있는 정보를 함부로 수정 할 수 없습니다.
    def __init__(self):
        self.__diceNumber = random.randint(DiceNumber.ONE.Value, DiceNumber.SIX.Value)

    def getDiceNumber(self):
        return self.__diceNumber