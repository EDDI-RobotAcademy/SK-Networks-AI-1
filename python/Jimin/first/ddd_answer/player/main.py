from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
from initializer.domain_initializer import DomainInitializer

# Domain 객체들을 초기화하는 작업
DomainInitializer.initEachDomain()


if __name__ == "__main__":
    firstPlayerId = 1

    diceRepository = DiceRepositoryImpl.getInstance()
    diceRepository.rollDice(firstPlayerId)

    firstPlayerDice = diceRepository.checkDice(firstPlayerId)
    print(f"첫 번째 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    print(f"첫 번째 주사위를 굴린 플레이어 id: {firstPlayerDice.getPlayerId()}")

    PlayerId = 1
    NickName = "Jimin"

    playerRepository = PlayerRepositoryImpl.getInstance()
    playerRepository.match(PlayerId, NickName)

    playerRepository.getPlayerId(PlayerId)
    firstId = playerRepository.getPlayerId(PlayerId)
    print(firstId) # <player.entity.player.Player object at 0x0000028C88282330>
    print(PlayerId) # 1
    firstNickname = playerRepository.getNickname(firstId)

    print(firstNickname)
