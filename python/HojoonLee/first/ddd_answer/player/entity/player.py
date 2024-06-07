class Player:
    def __init__(self):
        self.__playerNickname = None
        self.__playerId = 0

    def setPlayerNickname(self, playerNickname):
        self.__playerNickname = playerNickname
    def setPlayerId(self, playerId):
        self.__playerId = playerId
    def getPlayerNickname(self):
        return self.__playerNickname
    def getPlayerId(self):
        return self.__playerId