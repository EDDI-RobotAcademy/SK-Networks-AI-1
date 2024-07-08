from recurrent_neural_network.repository.rnn_repository_impl import RecurrentNeuralNetworkRepositoryImpl
from recurrent_neural_network.service.rnn_service import RecurrentNeuralNetworkService


class RecurrentNeuralNetworkServiceImpl(RecurrentNeuralNetworkService):
    VOCAB_SIZE = 65
    EMBEDDING_DIMENSION = 256
    RNN_UNITS = 1024
    BATCH_SIZE = 1

    def __init__(self):
        self.recurrentNeuralNetworkRepositoryImpl = RecurrentNeuralNetworkRepositoryImpl()

    def trainText(self):
        print('service -> trainText()')

        rnnModel = self.recurrentNeuralNetworkRepositoryImpl.createRnnModel(
            self.VOCAB_SIZE, self.EMBEDDING_DIMENSION, self.RNN_UNITS, self.BATCH_SIZE)
        buildRnnModel = self.recurrentNeuralNetworkRepositoryImpl.build(rnnModel, self.BATCH_SIZE)
        self.recurrentNeuralNetworkRepositoryImpl.printModelSummary(buildRnnModel)

        # compiledRnnModel = self.recurrentNeuralNetworkRepositoryImpl.compile(rnnModel)


