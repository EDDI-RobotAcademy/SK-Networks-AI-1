from dice.service.dice_service_impl import DiceServiceImpl
from initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl

# Domain 객체들을 초기화하는 작업
DomainInitializer.initEachDomain()


# Player Domain을 앞서 만들어봤습니다.
# 또한 수업 중 Dice Domain도 만들어봤습니다.
# Player 2명이 주사위를 굴리도록 만듭니다.
# 그리고 주사위의 눈금이 더 높은 사람이 게임에서 승리하도록 코드를 작성해봅시다.

def keepPlayerDomainInstance():
    global playerService
    playerService = PlayerServiceImpl.getInstance()

def keepDiceDomainInstance():
    global diceService
    diceService = DiceServiceImpl.getInstance()

def keepDomainInstance():
    keepPlayerDomainInstance()
    keepDiceDomainInstance()


def createPlayer(nickname):
    playerService.createPlayer(nickname)


if __name__ == "__main__":
    keepDomainInstance()

    firstPlayerNickname = "가즈아"
    createPlayer(firstPlayerNickname)

    secondPlayerNickname = "어디르"
    createPlayer(secondPlayerNickname)
