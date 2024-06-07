# print('깃 업로드 테스트 파이')

import random
# 주사위 클래스 생성
class Dice:
    MIN = 1
    MAX = 6
    def rollDice(self):
        print('MAX:', self.MAX)
        return random.randint(self.MIN, self.MAX)

dice = Dice()
dice_number = dice.rollDice()

print('주사위숫자:',dice_number)


class Player:
    playerId = 0
    def __init__(self, nickname):
        self.playerId += 1
        self.nickname = nickname

    def getPlayerId(self):
        return self.playerId

    def getNickname(self):
        return self.nickname

firstPlayer = Player('파이썬')
playerId = firstPlayer.getPlayerId()
nickname = firstPlayer.getNickname()
print('playerId:', playerId)
print('nickname:', nickname)


