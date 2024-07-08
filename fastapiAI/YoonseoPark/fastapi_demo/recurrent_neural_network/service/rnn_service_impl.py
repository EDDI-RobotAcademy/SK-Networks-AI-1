from recurrent_neural_network.repository.rnn_repository_impl import RecurrentNeuralNetworkRepositoryImpl
from recurrent_neural_network.service.rnn_service import RecurrentNeuralNetworkService


class RecurrentNeuralNetworkServiceImpl(RecurrentNeuralNetworkService):
    VOCAB_SIZE = 65
    EMBEDDING_DIMENSION = 256
    RNN_UNITS = 1024
    BATCH_SIZE = 1

    def __init__(self):
        self.recurrentNeuralNetworkRepository = RecurrentNeuralNetworkRepositoryImpl()

    def textTrain(self):
        print('service -> textTrain()')
        rnnModel = self.recurrentNeuralNetworkRepository.createRnnModel(
            self.VOCAB_SIZE, self.EMBEDDING_DIMENSION, self.RNN_UNITS, self.BATCH_SIZE)
        self.recurrentNeuralNetworkRepository.train(rnnModel, self.BATCH_SIZE)