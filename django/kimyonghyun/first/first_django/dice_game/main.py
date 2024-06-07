from initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl
from dice.service.dice__service__impl import DiceServiceImpl
from game.service.game_service_impl import GameServiceImpl

DomainInitializer.initDiceDomain()

def keepPlayerDomainInstance():
    global playerService
    playerService = PlayerServiceImpl.getInstance()

def keepDiceDomainInstance():
    global diceService
    diceService = DiceServiceImpl.getInstance()

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

    firstPlayerNickname = "메롱"
    createPlayer(firstPlayerNickname)

    secondPlayerNickname = "바보"
    createPlayer(secondPlayerNickname)

    gameService.registerGameResult()
    gameService.checkDiceGameWinner()
