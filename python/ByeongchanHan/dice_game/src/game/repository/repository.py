import abc


class GameRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, player_dice_map):
        pass

    @abc.abstractmethod
    def check_dice_game_winner(self):
        pass
