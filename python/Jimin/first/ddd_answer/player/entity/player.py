class Player:
    # '__' 언더바 두개는 접근 제한자의 역할로 private을 의미합니다.
    # 그러므로 외부에서 '__' 가 있는 정보를 함부로 수정 할 수 없습니다.
    def __init__(self):
        self.__playerNickname = None
        self.__playerId = None

    def setPlayerNickname(self, nickname):
        self.__playerNickname = nickname

    def setPlayerId(self, playerId):
        self.__playerId = playerId

    def getPlayerNickname(self):
        return self.__playerNickname

    def getPlayerId(self):
        return self.__playerId

