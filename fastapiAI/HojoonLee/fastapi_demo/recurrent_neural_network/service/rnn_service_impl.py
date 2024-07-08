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
        # rnn 모델 build
        buildRnnModel = self.recurrentNeuralNetworkRepositoryImpl.build(rnnModel, self.BATCH_SIZE)
        # rnn 모델 빌드 이후 모델 정보 보기
        self.recurrentNeuralNetworkRepositoryImpl.printModelSummary(buildRnnModel)
        # rnn모델 컴파일
        compiledRnnModel = self.recurrentNeuralNetworkRepositoryImpl.compile(rnnModel)

        # 가상의 입력 데이터 만들기
        virtualX, virtualY = self.recurrentNeuralNetworkRepositoryImpl.createData(self.VOCAB_SIZE, 1000, 100)
        # 모델 학습
        fittedRnnModel = self.recurrentNeuralNetworkRepositoryImpl.train(virtualX, virtualY, compiledRnnModel, self.BATCH_SIZE)
        # 모델 저장
        fittedRnnModel.save('rnn_model.h5')

    def predictText(self, inputText):
        print("service -> predictText()")

        # 학습모델 불러오기
        loadedModel = self.recurrentNeuralNetworkRepositoryImpl.loadModel()

        # 모델과 입력데이터로 추론하기
        return self.recurrentNeuralNetworkRepositoryImpl.generateText(loadedModel, inputText)