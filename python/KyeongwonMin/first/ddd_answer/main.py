from dice.repository.dice_repository_Impl import DiceRepositoryImpl
from initializer.domain_initializer import DomainInitializer

# Domain 객체들을 초기화하는 작업
# 커서를 놓고 [컨트롤+b]를 누르면 쓰여진 코드로 이동
DomainInitializer.initEachDomain()

if __name__ == "__main__":
    firstPlayerId = 5

    diceRepository = DiceRepositoryImpl.getInstance()
    diceRepository.rollDice(firstPlayerId)

    firstPlayerDice = diceRepository.checkDice(firstPlayerId)
    print(f"첫번째 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    print(f"첫번째 주사위를 굴린 플레이어 id: {firstPlayerId}")