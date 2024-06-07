import random
from dice.entity.DiceNumber import DiceNumber

class Dice:
    ## "__"언더바 두 개는 접근제한자의 역할로 private을 의미합니다.
    # 그러므로 외부에서 "__" 가 있는 정보를 함부로 수정 할 수 없습니다.
    ## 누군가 건들어서 complie 오류를 발생시키지 않기 위해서
    ## 버그 발생 접근제한자가
    def __init__(self):
       self.__diceNumber = random.randint(DiceNumber.ONE.value,DiceNumber.SIX.value)

    def getDiceNumber(self):
        return self.__diceNumber