from dice.repository.dice_repository_impl import DiceRepositoryImpl
from initializer.domain_initializer import DomainInitializer
import random 

DomainInitializer.initEachDomain()


if __name__ == "__main__":
    firstPlayerId = random.randint(1, 100)
    firstPlayerNickname = "이용우"  
    secondPlayerId = random.randint(101, 200)
    secondPlayerNickname = "LeeYongWoo"  

    diceRepository = DiceRepositoryImpl.getInstance()
    diceRepository.rollDice(firstPlayerId, firstPlayerNickname)  
    diceRepository.rollDice(secondPlayerId, secondPlayerNickname) 
    
    firstPlayerDice = diceRepository.checkDice(firstPlayerId)
    print(f"첫 번째 플레이어 닉네임: {firstPlayerDice.getPlayerNickname()}")  
    print(f"첫 번째 주사위를 굴린 플레이어 id: {firstPlayerDice.getPlayerId()}")
    print(f"첫 번째 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
    
    print()

    secondPlayerDice = diceRepository.checkDice(secondPlayerId)
    print(f"두 번째 플레이어 닉네임: {secondPlayerDice.getPlayerNickname()}") 
    print(f"두 번째 주사위를 굴린 플레이어 id: {secondPlayerDice.getPlayerId()}")
    print(f"두 번째 주사위 눈금: {secondPlayerDice.getDiceNumber()}")

    print()

    if (firstPlayerDice.getDiceNumber() > secondPlayerDice.getDiceNumber()):
        print(f"승자는 ", firstPlayerNickname)
    elif (firstPlayerDice.getDiceNumber() == secondPlayerDice.getDiceNumber()):
        print("무승부")
    else:
        print(f"승자는 ", secondPlayerNickname)
