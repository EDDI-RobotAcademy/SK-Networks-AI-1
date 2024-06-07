import random

class Dice: # 주사위 클래스
    MIN = 1
    MAX = 6

    def rollDice(self): # 주사위 굴리고 결과 반환
        print('MAX:', self.MAX)
        return random.randint(self.MIN, self.MAX)

dice = Dice()  # Dice 클래스의 인스턴스 생성
dice_number = dice.rollDice()
print("주사위 숫자:", dice_number)  # rollDice() 메소드 호출하여 결과 출력

class Player:
    playerId = 0
    nickname = None

    def __init__(self, nickname):
        Player.playerId += 1
        self.nickname = nickname

    def getPlayerId(self):
        return  self.playerId

    def getNickname(self):
        return  self.nickname

firstPlayer = Player("오늘 파이썬 처음")   # Player 클래스의 인스턴스 생성
playerId1 = firstPlayer.getPlayerId()
nickname1 = firstPlayer.getNickname()
print('playerId1:', playerId1)
print('nickname1:', nickname1)

secondPlayer = Player("두번째")
playerId2 = secondPlayer.getPlayerId()
nickname2 = secondPlayer.getNickname()
print('playerId2:', playerId2)
print('nickname2:', nickname2)

# self를 사용하면 각각의 객체들이 서로 자기 자신이 직접 가지고 있는 것을 의미함
# 객체A의 self는 A, 객체B의 self는 B
# 그러나 클래스이름(Player)을 가지고 사용하게 되면 A와 B는 모두 같은 클래스라는 전제 하에
# 공통적으로 가지고있는 정보 값을(playerId) 적용하게 됨