from initializer.domain_initializer import DomainInitializer

from dice.service.dice_service_impl import DiceServiceImpl
from player.service.player_service_impl import PlayerServiceImpl
from game.service.game_service_impl import GameServiceImpl

DomainInitializer.initEachDomain()


def keepDiceDomainInstance():
    global diceService
    diceService = DiceServiceImpl.getInstance()

def keepPlayerDomainInstance():
    global playerService
    playerService = PlayerServiceImpl.getInstance()

def keepGameDomainInstance():
    global gameService
    gameService = GameServiceImpl.getInstance()

def keepDomainInstance():
    keepDiceDomainInstance()
    keepPlayerDomainInstance()
    keepGameDomainInstance()


def createPlayer(nickname):
    playerService.createPlayer(nickname)


if __name__ == "__main__":
    keepDomainInstance()

    firstPlayerNickname = "1번사용자"
    createPlayer(firstPlayerNickname)

    secondPlayerNickname = "2번사용자"
    createPlayer(secondPlayerNickname)

    gameService.registerGameResult()
    gameService.checkDiceGameWinner()