from Initializer.domain_initializer import DomainInitializer
from player.service.player_service_impl import PlayerServiceImpl
from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
DomainInitializer.initEachDomain()

if __name__ == '__main__':
    # 기존 플레이어 도메인을 통해 두 명의 player를 만들고
    firstPlayerNickname = '첫번째플레이어'
    secondPlayerNickname = '두번째플레이어'
    playerService = PlayerServiceImpl.getInstance()

    # 첫 번째 product
    playerService.createPlayer(firstPlayerNickname)
    firstPlayer = playerService.findPlayerByNickname(firstPlayerNickname)
    # 두 번째 product
    playerService.createPlayer(secondPlayerNickname)
    secondPlayer = playerService.findPlayerByNickname(secondPlayerNickname)

    # 생성한 player의 playerId dice로 넘기고
    diceRepository = DiceRepositoryImpl.getInstance()
    # 첫 번쨰 player의 주사위 눈금
    diceRepository.rollDice(firstPlayer.getPlayerId())
    firstPlayerDice = diceRepository.checkDice(firstPlayer.getPlayerId())
    # 두 번째 player의 주사위 눈금
    diceRepository.rollDice(secondPlayer.getPlayerId())
    secondPlayerDice = diceRepository.checkDice(secondPlayer.getPlayerId())

    # 게임 도메인에서 주사위 결과를 받아서 눈금이 더 높으면 승리하는 코드
    gameRepository = GameRepositoryImpl.getInstance()
    winner = gameRepository.getWinner(firstPlayerDice, firstPlayer, secondPlayerDice, secondPlayer)
    print(winner)
