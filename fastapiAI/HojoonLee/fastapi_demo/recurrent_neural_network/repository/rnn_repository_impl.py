from recurrent_neural_network.repository.rnn_repository import RecurrentNeuralNetworkRepository
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from keras.models import load_model
import tensorflow as tf
import numpy as np
class RecurrentNeuralNetworkRepositoryImpl(RecurrentNeuralNetworkRepository):

    def createRnnModel(self, vocabSize, embeddingDimension, rnnUnits, batchSize):

        # 기본 RNN 구조로 설정
        model = Sequential([
            # Embedding은 text를 vector로 사상(mapping) 하는 작업입니다.
            # 그렇기에 실제 입베딩 보다는 mapToVector 혹은 textToVector 또는 TextRepresentation이란 표현이 더 좋은 것 같긴합니다.
            # Embedding Layer에서는 vocabSize를 지정하여 입력 차원을 지정합니다.
            # text 데이터에서 사용하는 고유 단어의 수가 vocabSize 만큼이라는 뜻입니다.

            # embeddingDimension의 경우 출력 차원에 해당합니다.
            # 각각의 단어들을 표현하기 위해 사용하는 벡터의 크기라고 보면 되겠습니다.

            # batch_input_shape의 경우엔 ㄴ입력 데이터의 형태를 의미합니다.
            # [batchSize, None]은 각 배치의 크기와 가변적인 시퀀스 길이를 의미합니다.
            # batchSize는 한 번에 처리할 샘플 숫자를 의미합니다.
            # 단어 하나하나를 정확하게 인식해야 하므로 당연히 '1'입니다.
            # 그리고 None은 시퀀스 길이가 가변적임을 의미합니다.(글자 길이가 고정이 아니란 소리)
            Embedding(vocabSize, embeddingDimension, batch_input_shape=[batchSize, None]),

            # rnnUnits의 경우 RNN Layer 숫자를 의미합니다.
            # 결론적으로 RNN 출력 벡터의 차원을 결정하게 됩니다.

            # return_sequences의 경우 시퀀스 전체를 출력으로 반환하도록 설정합니다.
            # 이는 다음 RNN Layer 혹은 Dense Layer 가 전체 시퀀스 자체를 입력으로 받을 수 있게 됩니다.

            # stateful의 경우 각각이 RNN 상태를 유지하도록 합니다.
            # 경계를 넘어서도 상태를 유지하여 상태값의 피드백이 끊기지 않도록 만듭니다.
            # 마지막으로 recurrent_initializer는 RNN의 가중치를 초기화합니다.
            # 이 때 초기화 방법으로 glorot uniform 방식을 사용합니다.

            # 사실 RNN은 대표적인 소위 '제어 공학' 이라 불리는 영역에서 '피드백 제어'와 매우 유사합니다.
            # 과거의 결과가 현재의 결과에 영향을 미치고 그 다음 결과에도 지속적으로 영향을 미치도록 만들기 때문입니다.
            # 즉 시간이 지남에 따라 순차적으로 생성된 정보를 모두 다시 입력하여 학습하는 시스템이 RNN이라고 볼 수 있습니다.
            # (전형적인 피드백 형태) -> 한 번 잘 못 학습하면 이후에 악영향이 큼
            SimpleRNN(rnnUnits, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform'),

            # Dense를 통해 출력벡터의 차원을 지정함
            # 입력에 대해 예측할 단어의 분포로 봐도 무방
            Dense(vocabSize)
        ])

        return model

    def compile(self, rnnModel):
        rnnModel.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
        return rnnModel

    def build(self, rnnModel, batchSize):
        print("repository -> train()")

        # 입력은 1 출력은 가변으로 설정
        rnnModel.build(tf.TensorShape([batchSize, None]))
        return rnnModel

    def printModelSummary(self, buildRnnModel):
        buildRnnModel.summary()

    def createData(self, vocabSize, numberOfSample, sequenceLength):
        xData = np.random.randint(0, vocabSize, (numberOfSample, sequenceLength))
        yData = np.roll(xData, shift=-1, axis=1)

        return xData, yData

    def train(self, x, y, compiledRnnModel, batchSize):
        compiledRnnModel.fit(x, y, epochs=1, batch_size=batchSize)
        return compiledRnnModel

    def loadModel(self):
        return load_model('rnn_model.h5')

    def generateText(self, loadedModel, inputText):
        # ord(char)를 통해 문자를 ASCII 코드로 변환합니다.
        # tf.expand_dims()를 통해 모델 입력에 맞게 차원을 확장합니다.
        numGenerate = 100

        # 65 범주 안에 넣을 수 있도록 inputText를 매칭시킴: text -> ascii화가 아닌 0~65로 범주화
        charToIndex = {data:index for index, data in enumerate(inputText)}
        # 중복 제거
        inputEval = [charToIndex[char] if char in charToIndex else 0 for char in inputText]
        tfInputEval = tf.expand_dims(inputEval, 0) # (5) -> (1,5)

        #inputEval = [ord(char) for char in inputText] # 숫자화 (ascii code)
        #tfinputEval = tf.expand_dims(inputEval, 0)
        #print(f"tfinputEval : {tfinputEval.shape}")

        # 생성된 텍스트 저장
        generatedText = []
        # 무작위성을 제어하기 위한 엔트로피용 변수 (값이 낮을 수록 더 예측 가능하며, 높을수록 무작위 성이 높아짐)
        # entropy tau(parameter)
        temperature = 1.0

        # 모델 상태 초기화
        loadedModel.reset_states()

        # 실질적인 텍스트 생성
        for index in range(numGenerate):
            predictions = loadedModel(tfInputEval)
            # tf.squeeze() 메서드는 쥐어 짜내는 것입니다 >> 차원을 축소
            # predictions 의 0차원 부분을 없앤다.
            # print(f"before predictions shape : {predictions.shape}")
            tfPredictions = tf.squeeze(predictions, 0) # [5, 65]
            # print(f"after predictions shape : {tfPredictions.shape}")

            entropicalPredictions = tfPredictions / temperature

            # 이 부분 알아보기
            if index == 0:
                print(f"이건 뭐지 : {tf.random.categorical(entropicalPredictions, num_samples=1)}")
                print(f"이건 뭐지2 : {tf.random.categorical(entropicalPredictions, num_samples=1)[-1]}")
                print(f"이건 뭐지3 : {tf.random.categorical(entropicalPredictions, num_samples=1)[-1, 0]}")
                # 여긴 numpy 화를 위함
                # print(f"이건 뭐지4 : {tf.random.categorical(entropicalPredictions, num_samples=1)[-1, 0].numpy()}")

            # tf.random.categorical 파트는 주어진 예측 확률 분포에서 하나의 문자를 무작위로 선택합니다. (num_samples=1)
            # 이 녀석은 num_samples의 샘플을 무작위로 선택합니다.
            # [-1, 0]의 의미는 굉장히 독특한데
            # [-1]은 마지막 배치를 선택
            # [0]은 첫 번째 샘플을 선택한다는 의미 >> 곧 마지막 배치의 첫 번째 샘플을 선택한다는 뜻
            # 즉, predictedId는 예측된 문자의 인덱스라고 보면 됨
            predictedId = tf.random.categorical(entropicalPredictions, num_samples=1)[-1, 0].numpy()

            tfInputEval = tf.expand_dims([predictedId], 0) # (predictedId = 1) -> (1,1)로 확장
            # print(f"tfInputEval : {tfInputEval.shape}")
            generatedText.append(chr(predictedId)) # 십진수 다시 문자화(list)

        return inputText + ''.join(generatedText) # list를 str로 바꿔서 이어줌