from player.service.player_service_impl import PlayerServiceImpl
from dice.service.dice_service_impl import DiceServiceImpl
from game.service.game_service_impl import GameServiceImpl


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