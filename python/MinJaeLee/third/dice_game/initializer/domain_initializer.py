from dice_game.dice.service.dice_service_impl import DiceServiceImpl
from dice_game.game.service.game_service_impl import GameServiceImpl
from dice_game.player.service.player_service_impl import PlayerServiceImpl


class DomainInitializer:
    @staticmethod
    def initPlayerDomain():
        PlayerServiceImpl.getInstance()

    @staticmethod
    def initDiceDomain():
        DiceServiceImpl.getInstance()

    @staticmethod
    def initGameDomain():
        GameServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initPlayerDomain()
        DomainInitializer.initDiceDomain()
        DomainInitializer.initGameDomain()
