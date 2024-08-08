class Player:
    def __init__(self, player_id, nickname):
        self.player_id = player_id
        self.nickname = nickname


class PlayerRepository:
    def __init__(self):
        self.players = {}

    def add(self, player):
        self.players[player.player_id] = player

    def get(self, player_id):
        return self.players.get(player_id)

user1 = Player('11','zz')
plrepo = PlayerRepository()
plrepo.add(user1)
print(plrepo.get('11').nickname)

class Game:
    def __init__(self):
        pass
    def getid(self, player1, player2):
        pass
    def roll(self):
        pass


