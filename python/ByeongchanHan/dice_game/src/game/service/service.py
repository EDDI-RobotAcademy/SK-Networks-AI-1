import abc


class GameService(abc.ABC):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def check_dice_game_winner(self):
        pass
