from .dice.service import DiceServiceImpl
from .game.service import GameServiceImpl
from .player.service import PlayerServiceImpl


class DomainInitializer:
    @staticmethod
    def init_dice_domain():
        DiceServiceImpl.get_instance()

    @staticmethod
    def init_player_domain():
        PlayerServiceImpl.get_instance()

    @staticmethod
    def init_game_domain():
        GameServiceImpl.get_instance()

    @staticmethod
    def init_each_domain():
        DomainInitializer.init_dice_domain()
        DomainInitializer.init_player_domain()
        DomainInitializer.init_game_domain()


DomainInitializer.init_each_domain()
