"""
Entity가 세부사항이 된다
현재는 playerId와 nickname만 가지고있지만,
만약 더 필요한 사항. 예를 들면 식별 번호나 결제 정보 등
추가 사항이 필요하다면 Entity에 추가해야함.
"""


class Player:
    __playerId = 0
    # playerId를 하나씩 증가시키기 위함
    __autoIncrementPlayerId = 0

    def __init__(self, nickname):
        # 생성될 때마다 값을 1씩 증가시키고
        Player.__autoIncrementPlayerId += 1
        # 그 증가된 값을 playerId에 할당
        self.__playerId = Player.__autoIncrementPlayerId
        # setter가 불필요함
        # >> '닉네임을 변경할 수 있다' 라는 agenda 자체가 없었기 때문.
        self.__nickname = nickname

    def getPlayerId(self):
        return self.__playerId

    def getPlayerNickname(self):
        return self.__nickname
