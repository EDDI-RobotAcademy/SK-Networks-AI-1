from recurrent_neural_network.repository.rnn_repository_impl import RecurrentNeuralNetworkRepositoryImpl
from recurrent_neural_network.service.rnn_service import RecurrentNeuralNetworkService

class RecurrentNeuralNetworkServiceImpl(RecurrentNeuralNetworkService):
    VOCAB_SIZE = 65
    EMBEDDING_DEMENSION = 256
    RNN_UNITS = 1024
    BATCH_SIZE = 1

    def __init__(self):
        self.recurrentNeuralNetworkRepositoryImpl = RecurrentNeuralNetworkRepositoryImpl()

    def trainText(self):
        print("service -> trainText()")

        # rnn 모델 생성
        rnnModel = self.recurrentNeuralNetworkRepositoryImpl.createRnnModel(self.VOCAB_SIZE, self.EMBEDDING_DEMENSION,
                                                                            self.RNN_UNITS, self.BATCH_SIZE)

        self.recurrentNeuralNetworkRepositoryImpl.train(rnnModel, self.BATCH_SIZE)