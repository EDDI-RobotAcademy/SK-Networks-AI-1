from dice.repository.dice_repository_impl import DiceRepositoryImpl
from initializer.domain_initializer import DomainInitializer

# Domain 객체들을 초기화하는 작업
DomainInitializer.initEachDomain()

if __name__ == "__main__":
    firstPlayerId = 5
    secondPlayerId = 6

    diceRepository = DiceRepositoryImpl.getInstance()  # 싱글톤 객체
    diceRepository.rollDice(firstPlayerId)
    diceRepository.rollDice(secondPlayerId)


    firstPlayerDice = diceRepository.checkDice(firstPlayerId)
    secondPlayerDice = diceRepository.checkDice(secondPlayerId)

    print(f"첫 번째 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    print(f"첫 번째 주사위를 굴린 플레이어 id: {firstPlayerDice.getPlayerId()}")
    print(f"두 번째 주사위 눈금: {secondPlayerDice.getDiceNumber()}")
    print(f"두 번째 주사위를 굴린 플레이어 id: {secondPlayerDice.getPlayerId()}")