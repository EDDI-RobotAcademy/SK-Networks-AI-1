from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

from recurrent_neural_network.repository.rnn_repository import RecurrentNeuralNetworkRepository

import tensorflow as tf


class RecurrentNeuralNetworkRepositoryImpl(RecurrentNeuralNetworkRepository):
    def train(self, rnnModel, batchSize):
        print('repository -> train()')

        rnnModel.build(tf.TensorShape([batchSize, None]))

    def createRnnModel(self, vocabSize, embeddingDimension, rnnUnits, batchSize):
        print('repository -> createRnnModel()')

        model = Sequential([
            # Embedding(임베딩)은 text를 vector로 사상(map) 하는 작업입니다.
            # 그렇기에 사실 임베딩 보다는 mapToVector 혹은 textToVector
            # 또는 TextRepresentation 이 더 좋은 것 같긴합니다.

            # Embedding Layer에서는 vocabSize를 지정하여 입력 차원을 지정합니다.
            # text 데이터에서 사용하는 고유 단어의 수가 vocabSize 만큼이라는 뜻입니다.

            # embeddingDimension의 경우 출력 차원에 해당합니다.
            # 각각의 단어들을 표현하기 위해 사용하는 벡터의 크기라 보면 되겠습니다.

            # batch_input_shape의 경우엔 입력 데이터의 형태를 의미합니다.
            # [batchSize, None] 은 각 배치의 크기와 가변적인 시퀀스 길이를 의미합니다.
            # batchSize는 한 번에 처리할 샘플 숫자를 의미합니다.
            # 단어 하나하나를 정확하게 인식해야 하므로 당연히 '1' 입니다.
            # 그리고 None은 시퀀스 길이가 가변적임을 의미합니다(글자 길이가 고정이 아니란 소리)
            Embedding(vocabSize, embeddingDimension, batch_input_shape=[batchSize, None]),

            # rnnUnits의 경우 RNN Layer 숫자를 의미합니다.
            # 결론적으로 RNN 출력 벡터의 차원을 결정하게 됩니다.

            # return_sequences의 경우 시퀀스 전체를 출력으로 반환하도록 설정합니다.
            # 이는 다음 RNN Layer 혹은 Dense Layer 가 전체 시퀀스 자체를 입력으로 받을 수 있게 만듭니다.

            # stateful의 경우 각각이 RNN 상태를 유지하도록 지원합니다.
            # 경계를 넘어서도 상태를 유지하여 상태값의 피드백이 끊기지 않도록 만듭니다.

            # 마지막으로 recurrent_initializer는 RNN의 가중치를 초기화합니다.
            # 이 때 초기화 방법으로 glorot uniform 방식을 사용합니다.

            # 사실 RNN은 대표적인 소위 '제어 공학' 이라 불리는 영역에서 '피드백 제어' 와 매우 유사합니다.
            # 과거의 결과가 현재의 결과에 영향을 미치고 그 다음 결과에도 지속적으로 영향을 미치도록 만들기 때문입니다.
            # 즉 시간이 지남에 따라 순차적으로 생성된 정보를 모두 다시 입력하여
            # 학습하는 시스템이 RNN 이라고 볼 수 있습니다.
            # (전형적인 피드백 형태죠)
            # <- 다른 것에 대비하여 데이터 품질이 굉장히 중요한 녀석 중 하나
            SimpleRNN(rnnUnits, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform'),
            
            # Dense를 통해 출력 벡터의 차원을 지정함
            # 입력에 대해 예측할 단어의 분포로 바라봐도 무방하겠음
            Dense(vocabSize)
        ])

        return model


