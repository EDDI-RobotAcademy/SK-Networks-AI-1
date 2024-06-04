from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
from initializer.domain_initializer import DomainInitializer

# Domain 객체들을 초기화하는 작업
DomainInitializer.initEachDomain()

if __name__ == "__main__":
    firstPlayerId = 5

    diceRepository = DiceRepositoryImpl.getInstance()
    diceRepository.rollDice(firstPlayerId)

    diceList = diceRepository.getDiceNumber(firstPlayerId)
    firstPlayerDice = diceRepository.checkDice(firstPlayerId)

    print(f"첫 번째 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    print(f"첫 번째 주사위를 굴린 플레이어 id: {firstPlayerDice.getPlayerId()}")

    secondPlayerId = 2
    secondPlayerNickname = 'jh'

    playerRepository = PlayerRepositoryImpl.getInstance()
    playerRepository.getPlayerList(secondPlayerId, secondPlayerNickname)
    secondPlayer = playerRepository.getPlayer(secondPlayerId)

    print(f"첫 번째 플레이어 ID: {secondPlayer.getPlayerId()}")
    print(f"첫 번째 플레이어 Nickname: {secondPlayer.getPlayerNickname()}")
