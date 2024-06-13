from dice.service.dice_service_impl import DiceServiceImpl
from player.service.player_service_impl import PlayerServiceImpl
from game.service.game_service_impl import GameServiceImpl
class DomainInitializer:
    @staticmethod
    def initDiceDomain():
        DiceServiceImpl.getInstance()

    @staticmethod
    def initPlayerDomain():
        PlayerServiceImpl.getInstance()
    @staticmethod
    def initGameDomain():
        GameServiceImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initDiceDomain()
        DomainInitializer.initPlayerDomain()
        DomainInitializer.initGameDomain()