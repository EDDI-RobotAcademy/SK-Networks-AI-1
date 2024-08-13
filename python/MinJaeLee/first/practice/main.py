            import random


class Dice:
    MIN = 1
    MAX = 6

    def roll_dice(self):
        return random.randint(self.MIN, self.MAX)


dice = Dice()
dice_num = dice.roll_dice()

print("주사위 숫자:", dice_num)


class Player:
    playerId = 0
    nickname = None

    def __init__(self, nk):
        self.playerId += 1
        self.nickname = nk

    def get_player_id(self):
        return self.playerId

    def get_nickname(self):
        return self.nickname


first_player = Player("python noob")
player_id = first_player.get_player_id()
nickname = first_player.get_nickname()
print('player id:', player_id)
print('nickname:', nickname)
