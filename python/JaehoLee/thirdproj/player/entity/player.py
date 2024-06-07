class Player:
    def __init__(self, player_id, nickname):
        self.player_id = player_id
        self.nickname = nickname
    def roll_dice(self, dice):
        return dice.roll()