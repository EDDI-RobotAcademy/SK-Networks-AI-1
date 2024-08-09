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

        virtualX, virtualY = self.recurrentNeuralNetworkRepositoryImpl.createData(
                                                            self.VOCAB_SIZE, 1000, 100)

        rnnModel = self.recurrentNeuralNetworkRepositoryImpl.createRnnModel(
            self.VOCAB_SIZE, self.EMBEDDING_DIMENSION, self.RNN_UNITS, self.BATCH_SIZE)
        buildRnnModel = self.recurrentNeuralNetworkRepositoryImpl.build(rnnModel, self.BATCH_SIZE)
        self.recurrentNeuralNetworkRepositoryImpl.printModelSummary(buildRnnModel)

        compiledRnnModel = self.recurrentNeuralNetworkRepositoryImpl.compile(buildRnnModel)
        fittedRnnModel = self.recurrentNeuralNetworkRepositoryImpl.train(
                            virtualX, virtualY, compiledRnnModel, self.BATCH_SIZE)
        fittedRnnModel.save('rnn_model.h5')

    def predictText(self, inputText):
        print('service -> predictText()')

        loadedRnnModel = self.recurrentNeuralNetworkRepositoryImpl.loadModel()
        print(f"loadedRnnModel: {loadedRnnModel}")
        return self.recurrentNeuralNetworkRepositoryImpl.generateText(loadedRnnModel, inputText)
