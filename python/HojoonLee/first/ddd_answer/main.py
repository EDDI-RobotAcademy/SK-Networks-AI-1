from dice.repository.dice_repository_impl import DiceRepositoryImpl
from initializer.domain_initializer import DomainInitializer

# 도메인 객체들을 초기화하는 작업
DomainInitializer.initEachDomain() # 함수위치에 ctrl + b하면 파고들어감
# 이미 여기서 getInstance()를 수행했음

if __name__ == "__main__":
    firstPlayerId = 1

    # 앞에서 이미 domain initializer를 선언했기 때문에
    # 여기는 나 앞에서 반환한 객체 사용할게 의 의미 (새로 객체를 생성하는게 아님)
    diceRepository = DiceRepositoryImpl.getInstance() # domaininitializer에서 만든 싱글톤 객체
    diceRepository.rollDice(firstPlayerId) #

    firstPlayerDice = diceRepository.checkDice(firstPlayerId) # firstPlayerId에 대한 주사위 정보 반환
    print(f"첫 번째 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    print(f"첫 번째 주사위를 굴린 플레이어 id: {firstPlayerDice.getPlayerId()}")

