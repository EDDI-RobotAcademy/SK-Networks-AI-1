import random


class Dice:
    MIN = 1
    MAX = 6

    def rollDice(self):
        return random.randint(self.MIN, self.MAX)

    # 무언가 잘못된 코드
    # 1과 6처럼 숫자를 고정으로 해버리면안된다.
    def rollDiceWrong(self):
        return random.randint(1, 6)


dice = Dice()
dice_number = dice.rollDice()

print("주사위 숫자:", dice_number)


class Player:
    playerId = 1

    def __init__(self, nickname):
        self.playerId += 1
        self.nickname = nickname

    def getPlayerId(self):
        return self.playerId

    def getNickname(self):
        return self.nickname


firstPlayer = Player("hoony")
playerId = firstPlayer.getPlayerId()
nickname = firstPlayer.getNickname()
print("playerId:", playerId)
print("nickname:", nickname)
