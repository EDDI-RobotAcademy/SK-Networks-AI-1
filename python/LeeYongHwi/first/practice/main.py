# 주사위 클래스 생성
import random


class Dice:
    Min = 1
    Max = 6

    def rollDice(self):
        return random.randint(self.Min, self.Max)


dice = Dice()
dice_number = dice.rollDice()

print("주사위 숫자:", dice_number)


class Player:
    playerId = 0
    nickname = None

    def __init__(self, nickname):
        Player.playerId += 1  # self를 쓰면 고유한 번호를 가지지 못함
        self.nickname = nickname

    def getPlayerId(self):
        return self.playerId

    def getNickname(self):
        return self.nickname


firstPlayer = Player('yong')
playerId = firstPlayer.getPlayerId()
nickname = firstPlayer.getNickname()
print("playerId:", playerId)
print("nickname:", nickname)