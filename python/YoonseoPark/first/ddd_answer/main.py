from dice.service.dice_service_impl import DiceServiceImpl
from game.service.game_service_impl import GameServiceImpl
from player.service.player_service_impl import PlayerServiceImpl

def keepPlayerDomainInstance():
    global playerService
    playerService = PlayerServiceImpl.getInstance()

def keepDiceDomainInstance():
    global diceService
    diceService = DiceServiceImpl.getInstance()

def keepGameDomainInstance():
    global  gameService
    gameService = GameServiceImpl.getInstance()

def keepDomainInstance():
    keepPlayerDomainInstance()
    keepDiceDomainInstance()
    keepGameDomainInstance()


def registerPlayer(nickname):
    playerService.registerPlayer(nickname)

if __name__ == "__main__":

    keepDomainInstance()

    # -------- 2명의 player 등록  --------
    firstPlayerNickname = "사용자1"
    registerPlayer(firstPlayerNickname)

    secondPlayerNickname = "사용자2"
    registerPlayer(secondPlayerNickname)

    # -------- 주사위 던지기  --------
    gameService.registerGameResult()
    gameService.checkDiceGameWinner()



