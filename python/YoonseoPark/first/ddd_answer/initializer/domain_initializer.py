from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl

class DomainInitializer:
    @staticmethod
    def initDiceDomain():
        DiceRepositoryImpl.getInstance()

    @staticmethod
    def initPlayerDomain():
        PlayerRepositoryImpl.getInstance()

    @staticmethod
    def initGameDomain():
        GameRepositoryImpl.getInstance()

    @staticmethod
    def initEachDomain():
        DomainInitializer.initDiceDomain()
