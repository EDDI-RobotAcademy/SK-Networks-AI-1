# thirdproj/initailizer/initializer.py

from player.entity.player import  Player
from player.repository.player_repository import PlayerRepository

def initialize_players():
    player_repo = PlayerRepository()
    player1 = Player('1', '부처')
    player2 = Player('2', '예수')

    player_repo.add(player1)
    player_repo.add(player2)

    return player_repo

