from recurrent_neural_network.repository.rnn_repository_impl import RecurrentNeuralNetworkRepositoryImpl
from recurrent_neural_network.service.rnn_service import RecurrentNeuralNetworkService


class RecurrentNeuralNetworkServiceImpl(RecurrentNeuralNetworkService):
    VOCAB_SIZE = 65 # output 범주 0~65까지
    EMBEDDING_DIMENSION = 256 # 데이터가 바로 gpu에 올라오는게 아니라 올리기 위해 변환하는 과정
    RNN_UNITS = 1024 # RNN 히든 레이어를 몇개 할꺼냐
    BATCH_SIZE = 1 # 한번에 한 글자씩 하겠다.

    def __init__(self):
        self.recurrentNeuralNetworkRepository = RecurrentNeuralNetworkRepositoryImpl()
    def trainText(self):
        # print("service -> trainText()")

        virtualX, virtualY = self.recurrentNeuralNetworkRepository.createData(self.VOCAB_SIZE, 1000, 100)

        # rnn 모델 생성
        rnnModel = self.recurrentNeuralNetworkRepository.createRnnModel(self.VOCAB_SIZE, self.EMBEDDING_DIMENSION,
                                                                        self.RNN_UNITS, self.BATCH_SIZE)

        buildRnnModel = self.recurrentNeuralNetworkRepository.build(rnnModel, self.BATCH_SIZE)
        self.recurrentNeuralNetworkRepository.printModelSummary(buildRnnModel)

        compiledRnnModel = self.recurrentNeuralNetworkRepository.compile(buildRnnModel)

        # fitting해서 model자체 save 하기
        fittedRnnModel = self.recurrentNeuralNetworkRepository.train(virtualX, virtualY, compiledRnnModel, self.BATCH_SIZE)

        fittedRnnModel.save('rnn_model.h5')

    def predictText(self, inputText):
        print("service -> predictText()")

        # 학습된 파일 불러오기
        loadedModel = self.recurrentNeuralNetworkRepository.loadModel()
        return self.recurrentNeuralNetworkRepository.generateText(loadedModel, inputText)



