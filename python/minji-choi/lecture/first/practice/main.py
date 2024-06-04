#4. 주사위 클래스를 작성하세요.
import random

class Dice:
    MAX = 6
    MIN = 1
    def __init__(self, dice):
        self.dice = dice

    # 5. 주사위를 굴리는 서비스 코드를 작성하세요.
    def roll_dice(self):
        result = []
        for i in range(self.dice):
            dice_result = random.randint(self.MIN, self.MAX) # 프로그램을 만들 때 상수값을 바로 집어넣는 것은위험함!
            result.append(dice_result)
        return result

# 사용자 클래스
class Player:
    speNum = 0
    nickname = None
    def __init__ (self, nickname):
        Player.speNum +=1  # 이렇게 하면 플레이어마다 고유한 번호를 갖게 됨
        self.nickname = nickname

    def getSpeNum(self):
        return self.speNum
    def getnickname(self):
        return self.nickname

# 사용자가 주사위를 굴리는 클래스
class PlayerDice(Dice, Player):
    def __init__(self, dice, nickname):
        Dice.__init__(self, dice)
        Player.__init__(self, nickname)

    def player_roll(self):
        Player = self.roll_dice()
        p = f'고유번호 {self.speNum} 닉네임 {self.nickname} : 주사위 {self.dice}개 굴린 결과 {Player}가 나왔습니다.'
        print(p)


if __name__ == '__main__':
    u1 = PlayerDice(3, 'minn')
    u1.player_roll()

    u2 = PlayerDice(4, 'ji')
    u2.player_roll()

    # d1 = Dice(4)
    # print(d1.roll_dice())
