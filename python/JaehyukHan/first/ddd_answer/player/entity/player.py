class Player:
    def __init__(self):
        self.__playerId = None
        self.__nickname = None

    def setPlayerId(self, playerId):
        self.__playerId = playerId

    def getPlayerId(self):
        return self.__playerId

    def setPlayerNickname(self, nickname):
        self.__nickname = nickname

    def getPlayerNickname(self):
        return self.__nickname
