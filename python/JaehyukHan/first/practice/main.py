import random


# 주사위 클래스 생성
class Dice:
    MIN = 1
    MAX = 6
    def rollDice(self):
        return random.randint(self.MIN, self.MAX)


dice = Dice()
dice_number = dice.rollDice()

# print("주사위 숫자:", dice_number)


# 사용자 클래스 생성
"""
객체(Object)란?

메모리에 할당된 것 >> C에서의 malloc(), Java의 new()와 같다.

배경지식이 없는 경우, 어떠한 사물을 생각하자.
아래에 Player("파이썬은 처음인가요?") 부분이 객체를 생성하는 부분.
앞에서 언급한 것처럼 객체를 생성했기 때문에, firstPlayer는 객체가 됨
"""

"""
self란?

'객체가 자기 자신을 지칭하는 것'
사람의 경우엔 '나'라고 하지만, 객체의 경우엔 자기 자신은 'self'라고 지칭함.
"""
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


firstPlayer = Player("파이썬은 처음인가요?")
playerId = firstPlayer.getPlayerId()
nickname = firstPlayer.getNickname()

print("playerId:", playerId)
print("nickname:", nickname)

secondPlayer = Player("이게 뭐야")
secondPlayerId = secondPlayer.getPlayerId()
secondNickname = secondPlayer.getNickname()

print("second playerId:", secondPlayerId)
print("second nickname:", secondNickname)


