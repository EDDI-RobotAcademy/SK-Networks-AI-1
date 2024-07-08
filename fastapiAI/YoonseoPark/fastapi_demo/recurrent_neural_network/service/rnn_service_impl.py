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

        virtualX, virtualY = self.recurrentNeuralNetworkRepository.createData(self.VOCAB_SIZE, 1000, 100)

        rnnModel = self.recurrentNeuralNetworkRepository.createRnnModel(
            self.VOCAB_SIZE, self.EMBEDDING_DIMENSION, self.RNN_UNITS, self.BATCH_SIZE)

        buildRnnModel = self.recurrentNeuralNetworkRepository.build(rnnModel, self.BATCH_SIZE)
        self.recurrentNeuralNetworkRepository.printModelSummary(buildRnnModel)

        compiledRnnModel = self.recurrentNeuralNetworkRepository.compile(rnnModel)
        fittedRnnModel = self.recurrentNeuralNetworkRepository.train(
            virtualX, virtualY, compiledRnnModel, self.BATCH_SIZE)

        fittedRnnModel.save('rnn_model.h5')

    def textPredict(self, inputText):
        print('service -> textPredict()')

        loadedRnnModel = self.recurrentNeuralNetworkRepository.loadModel()
        return self.recurrentNeuralNetworkRepository.generateText(loadedRnnModel, inputText)



