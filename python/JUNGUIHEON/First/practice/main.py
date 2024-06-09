# 주사위 클래스 생성
import random
class Dice:
    MIN = 1
    MAX = 6
    def rollDice(self):
        print("MIN: ", self.MIN)
        print("MAX: ", self.MAX)
        return random.randint(self.MIN, self.MAX) # 상수값을 그대로 사용하는것은 위험

dice = Dice()
dice_number = dice.rollDice()

print("주사위 숫자 : ", dice_number)
print("\n")

class Player:
    playerId = 0
    nickname = None
    def __init__(self, nickname):
        Player.playerId += 1
        self.nickname = nickname

    def getPlayerId(self):
        return self.playerId

    def getNickname(self):
        return self.nickname

firstPlayer = Player("오늘파이썬처음")
firstplayerId = firstPlayer.getPlayerId()
firstnickname = firstPlayer.getNickname()
print("playerId: ", firstplayerId)
print("nickname: ", firstnickname)

secondPlayer = Player("오늘파이썬두번째")
secondplayerId = secondPlayer.getPlayerId()
secondnickname = secondPlayer.getNickname()
print("playerId: ", secondplayerId)
print("nickname: ", secondnickname)
