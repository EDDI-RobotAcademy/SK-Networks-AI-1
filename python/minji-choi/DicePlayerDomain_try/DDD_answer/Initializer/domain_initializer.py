from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.service.player_service_impl import PlayerServiceImpl
from game.repository.game_repository_impl import GameRepositoryImpl
class DomainInitializer:
    @staticmethod
    def initDiceDomain():
        DiceRepositoryImpl.getInstance()

    @staticmethod
    def initPlayerDomain():
        PlayerServiceImpl.getInstance()
    @staticmethod
    def initGameDomain():
        GameRepositoryImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initDiceDomain()
        DomainInitializer.initPlayerDomain()
        DomainInitializer.initGameDomain()