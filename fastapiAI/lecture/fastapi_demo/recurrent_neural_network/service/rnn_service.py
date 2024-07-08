from abc import ABC, abstractmethod


class RecurrentNeuralNetworkService(ABC):
    @abstractmethod
    def trainText(self):
        pass
