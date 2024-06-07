# 주사위 클래스 생성
import random

class Dice:
    min, max = 1,6
    def roll(self):
        return random.randint(self.min,self.max)
        # 상수를 그대로 할당하면 문제가 생길 수 있음 (1,6) >> (1, self.max)
        # 현업에서는 여러가지 변수로 인해 들어오는 값이 달라질 수 있기 때문에, 상수로 선언해서는 안됨
        # 상수로 하면 확장 이후 상수로 선언한 것을 다 바꿔야 함

dice = Dice()
dice_number = dice.roll()
print("주사위 숫자: ", dice_number)

class Player:
    PlayerId = 0
    def __init__(self, nickname):
        Player.PlayerId += 1 # self로 하면 모든 사람의 id가 다 1로 출력됨
        self.nickname = nickname
    def getPlayerId(self):
        return self.PlayerId
    def getNickname(self):
        return self.nickname

player1 = Player('sy')
playerid = player1.getPlayerId()
playername = player1.getNickname()
print("playerId : ", playerid)
print("nickname : ", playername)
player2 = Player('sy')
playerid2 = player2.getPlayerId()
print("playerId : ", playerid2)