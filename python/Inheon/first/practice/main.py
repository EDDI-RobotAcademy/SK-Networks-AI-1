# 주사위 클래스 생성
import random

class Dice:
    # dice_number = 0
    MIN = 1
    MAX = 6
    def rollDice(self):
        # return random.randint(1, 6) # 이렇게 직접적으로 상수를 코드에 사용할 경우, 매우 곤란한 경우가 생길 수 있음.
        print('MAX:', self.MAX)
        print('MIN:', self.MIN)
        return random.randint(self.MIN, self.MAX) # 따라서 이와 같이 변수로 지정해주는 것이 바람직한 방향임.
dice = Dice()
dice_number = dice.rollDice()

print('주사위 숫자:', dice_number)

class Player:
    playerId = 0
    nickname = None

    def __init__(self, nickname):
        self.playerId += 1
        self.nickname = nickname

    def getPlayerId(self):
        return self.playerId

    def getNickname(self):
        return self.nickname

firstPlayer = Player("오늘파이썬처음")
playerId = firstPlayer.getPlayerId()
nickname = firstPlayer.getNickname()
print('playerId:', playerId)
print('nickName:', nickname)