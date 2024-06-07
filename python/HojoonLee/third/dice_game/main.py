from dice.service.dice_service_impl import DiceServiceImpl
from game.service.game_service_impl import GameServiceImpl
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

def keepGameDomainInstance():
    global gameService
    gameService = GameServiceImpl.getInstance()

def keepDomainInstance():
    keepPlayerDomainInstance()
    keepDiceDomainInstance()
    keepGameDomainInstance()

def createPlayer(nickname):
    playerService.createPlayer(nickname) # player domain의 service로 ㄱㄱ


if __name__ == "__main__":
    keepDomainInstance() # 각 도메인 초기화과정 싱글톤으로 한번씩만 부르기

    # 사용자 지정
    firstPlayerNickname = "가즈아"
    createPlayer(firstPlayerNickname)

    secondPlayerNickname = "어디로"
    createPlayer(secondPlayerNickname)

    # 게임 결과 판정 및 저장
    gameService.registerGameResult()
    # 게임 결과 체크! (사실 위와 크게 다를건 없음)
    gameService.checkDiceGameWinner()
