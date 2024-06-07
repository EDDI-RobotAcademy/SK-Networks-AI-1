from Initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl
from dice.service.dice_service_impl import DiceServiceImpl
from game.service.game_service_impl import GameServiceImpl

DomainInitializer.initEachDomain()

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
    keepPlayerDomainInstance()
    keepDiceDomainInstance()
    keepGameDomainInstance()

def createPlayer(nickname):
    playerService.createPlayer(nickname)


if __name__ == '__main__':
    keepDomainInstance()

    firstPlayerNickname = "첫번째플레이어"
    createPlayer(firstPlayerNickname)

    secondPlayerNickname = "두번째플레이어"
    createPlayer(secondPlayerNickname)

    gameService.registerGameResult()
    gameService.checkDiceGameWinner()


