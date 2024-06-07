class Player:
    def __init__(self, player_id, nickname):
        self.__player_id = player_id
        self.__nickname = nickname

    def get_player_id(self):
        return self.__player_id

    def get_nickname(self):
        return self.__nickname