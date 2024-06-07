class Player:
    # '__' 언더바 두개는 접근 제한자의 역할로 private을 의미합니다.
    # 그러므로 외부에서 '__' 가 있는 정보를 함부로 수정 할 수 없습니다.
    __playerId = 0
    def __init__(self, nickname):
        self.__playerId += 1
        self.__nickname = nickname

    # 위에서 했듯이 코드를 짜주면 set을 따로 해 줄 필요가 없다.
    # 닉네임 변경이 필요한 아젠다가 없기 때문이다.

    def getPlayerNickname(self):
        return self.__nickname

    def getPlayerId(self):
        return self.__playerId

