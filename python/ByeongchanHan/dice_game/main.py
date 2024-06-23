from src.dice.service import DiceServiceImpl
from src.game.service import GameServiceImpl
from src.player.service import PlayerServiceImpl


def keep_dice_domain_instance():
    global dice_service
    dice_service = DiceServiceImpl.get_instance()


def keep_player_domain_instance():
    global player_service
    player_service = PlayerServiceImpl.get_instance()


def keep_game_domain_instance():
    global game_service
    game_service = GameServiceImpl.get_instance()


def keep_domain_instance():
    keep_dice_domain_instance()
    keep_player_domain_instance()
    keep_game_domain_instance()


if __name__ == "__main__":
    keep_domain_instance()

    game_service.register_players("a", "b", "c", "d", "e")
    game_service.play()
    game_service.check_dice_game_winner()
