from initalizer.initializer import initialize_players
from game.service.game_service import GameService

def main():
    player_repo = initialize_players()
    game_service = GameService(player_repo)

    result = game_service.play_game('1', '2')
    print(result)

if __name__ == "__main__":
    main()
