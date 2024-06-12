import abc


class DiceRepository(abc.ABC):
    @abc.abstractmethod
    def roll_dice(self):
        pass

    @property
    @abc.abstractmethod
    def dice_list(self):
        pass
