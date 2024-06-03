#4. 주사위 클래스를 작성하세요.
import random

class Dice:
    def __init__(self, dice):
        self.dice = dice

    # 5. 주사위를 굴리는 서비스 코드를 작성하세요.
    def roll_dice (self, dice):
        result = []
        for i in range(dice):
            dice = random.randint(1,6)
            result.append(dice)
        return result

# 사용자 클래스
class User:
    def __init__ (self, spe_num, nname):
        self.spe_num = spe_num
        self.nname = nname

# 사용자가 주사위를 굴리는 클래스
class UserDice(Dice, User):
    def __init__(self, dice, spe_num, nname):
        Dice.__init__(self, dice)
        User.__init__(self, spe_num, nname)

    def user_roll_dice(self):
        user = self.roll_dice(self.dice)
        p = f'고유번호 {self.spe_num} 닉네임 {self.nname} : 주사위 {self.dice}개 굴린 결과 {user}가 나왔습니다.'
        print(p)


if __name__ == '__main__':
    user = UserDice(3, 23, 'minn')
    user.user_roll_dice()
