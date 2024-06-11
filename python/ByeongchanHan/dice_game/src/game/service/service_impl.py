from src.dice.repository import DiceRepositoryImpl
from src.game.repository import GameRepositoryImpl
from src.player.repository import PlayerRepositoryImpl

from .service import GameService


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__game_repository = GameRepositoryImpl.get_instance()
            cls.__instance.__dice_repository = DiceRepositoryImpl.get_instance()
            cls.__instance.__player_repository = PlayerRepositoryImpl.get_instance()

        return cls.__instance

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def register_players(self, *nicknames):
        for nickname in nicknames:
            self.__player_repository.create(nickname)

    def play(self):
        player_list = self.__player_repository.player_list
        for _ in range(len(player_list)):
            self.__dice_repository.roll_dice()

        dice_list = self.__dice_repository.dice_list

        player_dice_map = {
            player.nickname: dice.dice_number
            for player, dice in zip(player_list, dice_list)
        }

        for result in player_dice_map:
            print(f"{result}: {player_dice_map[result]}")

        self.__game_repository.save(player_dice_map)

    def check_dice_game_winner(self):
        self.__game_repository.check_dice_game_winner()
