from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameResult = {} # hash니까 dict 형태로
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def save(self, playerDiceMap):
        self.__gameResult = playerDiceMap # dict에 추가

    def checkDiceGameWinner(self):
        maxDiceNumber = max(self.__gameResult.values()) # dict인 __gameResult의 value 추출
        # {}의 정보를 player, dice로 받아주고 for loop => 이때 max값과 같은 경우의 player를 반환
        maxPlayerList = [player for player, dice in self.__gameResult.items() \
                         if dice == maxDiceNumber]
        if len(maxPlayerList) > 1:
            print("무승부입니다!")
            return
        # tip if else 형태보다는 if if if 형태가 더 좋습니다.
        # if
        #   if 형태의 다단 들여쓰기 형식 아님
        # 협업이나 깃허브 제출할 때 이렇게 해라
        print(f"승자: {maxPlayerList[0]}")