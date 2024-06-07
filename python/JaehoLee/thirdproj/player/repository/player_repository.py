class PlayerRepository:
    def __init__(self):
        self.players = {}

    def add(self, player):
        self.players[player.player_id] = player
    def get(self, player_id):
        return self.players.get(player_id)
