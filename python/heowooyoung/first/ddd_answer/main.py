# from dice.repository.dice_repository_impl import DiceRepositoryImpl
# from initializer.domain_initializer import DomainInitializer
#
# # Domain 객체들을 초기화하는 작업
# DomainInitializer.initEachDomain()
# 
#
# if __name__ == "__main__":
#     firstPlayerId = 5
#
#     diceRepository = DiceRepositoryImpl.getInstance()
#     diceRepository.rollDice(firstPlayerId)
#
#     firstPlayerDice = diceRepository.checkDice(firstPlayerId)
#     print(f"첫 번째 주사위 눈금: {firstPlayerDice.getDiceNumber()}")
#     print(f"첫 번째 주사위를 굴린 플레이어 id: {firstPlayerDice.getPlayerId()}")

##############################################################################

from initializer.domain_initalizer import DomainInitializer
from player.repository.player_repository_impl import PlayerRepositoryImpl

# Domain 객체들을 초기화하는 작업
DomainInitializer.init_each_domain()

def main():
    player_repository = PlayerRepositoryImpl.get_instance()

    # 플레이어 추가
    player_repository.add_player(1, "하이")
    player_repository.add_player(2, "바이")

    # playerId를 통해 nickname 출력
    first_player = player_repository.get_player_by_id(1)
    second_player = player_repository.get_player_by_id(2)

    print(f"첫 번째 플레이어: {first_player.get_nickname() if first_player else '플레이어를 찾을 수 없습니다.'}")
    print(f"두 번째 플레이어: {second_player.get_nickname() if second_player else '플레이어를 찾을 수 없습니다.'}")

if __name__ == "__main__":
    main()



