from recurrent_neural_network.repository.rnn_repository_impl import RecurrentNeuralNetworkRepositoryImpl
from recurrent_neural_network.service.rnn_service import RecurrentNeuralNetworkService


class RecurrentNeuralNetworkServiceImpl(RecurrentNeuralNetworkService):

    VOCAB_SIZE = 65     # 아웃풋의 아스키코드 범주 (0~65까지)
    EMBEDDING_DIMENSION = 256       # 임베딩이란? 데이터는 바로 gpu에 올라갈 수 없기 때문에 gpu에 올릴 수 있도록 처리를 해주는 것
    RNN_UNITS = 1024        # RNN_UNITS는 RNN의 히든 레이어를 몇개를 할 것이냐
    BATCH_SIZE = 1      # ????????

    def __init__(self):
        self.recurrentNeuralNetworkRepositoryImpl = RecurrentNeuralNetworkRepositoryImpl()

    def textTrain(self):
        print('service -> textTrain()')

        # 가상의 데이터 생성
        virtualX,virtualY, = self.recurrentNeuralNetworkRepositoryImpl.createData(self.VOCAB_SIZE,1000,100)

        # 모델 생성
        rnnModel = self.recurrentNeuralNetworkRepositoryImpl.createRnnModel(
            self.VOCAB_SIZE, self.EMBEDDING_DIMENSION, self.RNN_UNITS, self.BATCH_SIZE)

        buildRnnModel = self.recurrentNeuralNetworkRepositoryImpl.build(rnnModel, self.BATCH_SIZE)

        self.recurrentNeuralNetworkRepositoryImpl.printModelSummary(buildRnnModel)

        compiledRnnModel = self.recurrentNeuralNetworkRepositoryImpl.compile(buildRnnModel)
        fittedRnnModel = self.recurrentNeuralNetworkRepositoryImpl.train(virtualX, virtualY, compiledRnnModel,self.BATCH_SIZE)

        fittedRnnModel.save('rnn_model.h5')

    def predictText(self, inputText):
        print('service -> predictText()')

        # 학습 모델 불러오기
        loadedRnnModel = self.recurrentNeuralNetworkRepositoryImpl.loadModel()
        print(f"loadedRnnModel: {loadedRnnModel}")

        #
        return self.recurrentNeuralNetworkRepositoryImpl.generateText(loadedRnnModel, inputText)
