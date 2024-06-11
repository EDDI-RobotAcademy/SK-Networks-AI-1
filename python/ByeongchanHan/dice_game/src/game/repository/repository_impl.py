from .repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__game_result = {}

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def save(self, player_dice_map):
        self.__game_result = player_dice_map

    def check_dice_game_winner(self):
        max_dice_number = max(self.__game_result.values())
        max_player_list = [
            player
            for player, dice_number in self.__game_result.items()
            if dice_number == max_dice_number
        ]

        if len(max_player_list) > 1:
            print("drow")
            return

        print(f"winner: {max_player_list[0]}")
