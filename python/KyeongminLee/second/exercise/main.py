from game.service.game_service_impl import GameServiceImpl
from initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl
from dice.service.dice_service_impl import DiceServiceImpl

# Domain 객체들을 초기화하는 작업
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

if __name__ == "__main__":
    keepDomainInstance()

    firstPlayerNickname = "001"
    createPlayer(firstPlayerNickname)

    secondPlayerNickname = "002"
    createPlayer(secondPlayerNickname)

    gameService.registerGameResult()
    gameService.checkDiceGameWinner()
