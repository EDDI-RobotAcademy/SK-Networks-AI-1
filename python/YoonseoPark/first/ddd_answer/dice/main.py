from dice.repository.dice_repository_impl import DiceRepositoryImpl
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