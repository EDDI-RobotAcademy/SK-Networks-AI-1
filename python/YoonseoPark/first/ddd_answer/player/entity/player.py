class Player:

    def __init__(self):
        self.__playerId = None
        self.__nickname = None

    def setPlayerId(self, playerId):
        self.__playerId = playerId

    def setNickname(self, nickname):
        self.__nickname = nickname

    def getPlayerId(self):
        return self.__playerId

    def getNickname(self):
        return self.__nickname
