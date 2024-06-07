from dice.repository.dice_repository_impl import DiceRepositoryImpl
from initializer.domain_initializer import DomainInitializer
from player.repository.player_repository_impl import PlayerRepositoryImpl


# Domain 객체들을 초기화하는 작업
DomainInitializer.initEachDomain()


if __name__ == "__main__":
    firstPlayerId = 5

    diceRepository = DiceRepositoryImpl.getInstance()
    diceRepository.rollDice(firstPlayerId)

    firstPlayerDice = diceRepository.checkDice(firstPlayerId)
    print(f"첫 번째 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    print(f"첫 번째 주사위를 굴린 플레이어 id: {firstPlayerDice.getPlayerId()}")



    playerRepository = PlayerRepositoryImpl.getInstance()

    firstPId = 7
    firstPlayerNickname = 'Son'
    secondPId = 19
    secondPlayerNickname = 'Kang In'


    playerRepository.checkPlayer(firstPId, firstPlayerNickname)
    playerRepository.checkPlayer(secondPId, secondPlayerNickname)

    firstPlayer = playerRepository.getPlayerId(firstPId)
    secondPlayer = playerRepository.getPlayerId(secondPId)

    print(f"첫 번째 플레이어 : {firstPlayer.getPlayerId(), firstPlayer.getNickname()}")
    print(f"두 번째 플레이어 : {secondPlayer.getPlayerId(), secondPlayer.getNickname()}")

