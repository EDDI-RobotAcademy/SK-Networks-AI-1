# 주사위 클래스 생성
import random

class Dice:
    MIN = 1
    MAX = 6

    def rollDice(self):
        return random.randint(self.MIN, self.MAX)

dice = Dice()
dice_number = dice.rollDice()

print("주사위 숫자: ", dice_number)

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

firstPlayer = Player("001")
playerId = firstPlayer.getPlayerId()
nickname = firstPlayer.getNickname()
print('playerID: ', playerId)
print('nickname: ', nickname)

firstPlayer = Player("002")
playerId = firstPlayer.getPlayerId()
nickname = firstPlayer.getNickname()
print('playerID: ', playerId)
print('nickname: ', nickname)