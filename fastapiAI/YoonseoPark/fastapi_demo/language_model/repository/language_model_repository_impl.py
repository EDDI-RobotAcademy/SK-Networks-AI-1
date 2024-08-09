import os

import numpy as np
import tensorflow

import tensorflow as tf
from keras import Sequential
from keras.src.callbacks import ModelCheckpoint
from keras.src.layers import Embedding, LSTM, Dense
from keras.src.losses import sparse_categorical_crossentropy
from tensorflow.keras.models import load_model

from language_model.repository.language_model_repository import LanguageModelRepository


class LanguageModelRepositoryImpl(LanguageModelRepository):
    SEQUENCE_LENGTH = 100

    BATCH_SIZE = 64
    BUFFER_SIZE = 10000

    EMBEDDING_DIM = 256
    RNN_UNITS = 1024

    EPOCHS = 20

    SHAKESPEARE_MODEL_PATH = "shakespeare_model.h5"

    GENERATION_COUNT = 1000

    # 고유 문자 목록 생성
    # 고유 문자를 추출하여 정렬된 리스트를 만들고자 하는 것이 이 부분의 목적임
    # 각 문자에 고유한 인덱스를 할당하고 문자 인덱스를 역변환 할 수 있도록 구성함
    # 그렇다면 추론이 정확하다는 가정하에 숫자값을 문자값으로 만들 수 있기 때문임
    def preprocessForCreateUniqueCharacter(self, text):
        characterList = sorted(list(set(text)))
        charToIndex = {character: index for index, character in enumerate(characterList)}
        indexToChar = np.array(characterList)

        return characterList, charToIndex, indexToChar

    # 텍스트를 입력 받아서 각 문자들을 대응하는 인덱스로 변환함
    def preprocessForCreateTextIndex(self, text, charToIndex):
        return np.array([charToIndex[character] for character in text])

    # 변환된 문자 인덱스를 TensorFlow에서 사용할 수 있는 형태로 만듭니다.
    # 마지막 문자는 제거하는 형식으로 구성함
    # 결론적으로 딥러닝 모델에 입력할 수 있는 형태를 만들기 위한 작업
    # 그러므로 텍스트를 숫자인 인덱스로 변환함
    # 이 인덱스를 가지고 시퀀스(문장의 일부)로 나눔 (self.SEQUENCE_LENGTH 가지고 몫 구하는 것)
    # 이후 입력과 타겟으로 나누는 작업을 진행함
    def createDataSet(self, text, textAsIndex):
        examplesForEpoch = len(text) // self.SEQUENCE_LENGTH
        # examplesForEpoch는 결론적으로 주어진 텍스트 데이터를 가지고 생성할 수 있는 문장 일부를 나타냄
        # 고로 100자씩 끊어치기함
        characterDataSet = tf.data.Dataset.from_tensor_slices(textAsIndex)
        # from_tensor_slices()는 배열을 텐서 플로우가 사용할 수 있는 형태의 배열로 만듬
        # 예로 [32, 1, 54, 23, 17, 3] 이라면 동일하게 32, 1, 54, 23, 17, 3을 순차적으로 반환함
        sequenceList = characterDataSet.batch(self.SEQUENCE_LENGTH + 1, drop_remainder=True)
        # 그리고 이 부분 때문에 사실 정확도가 떨어지게 됨
        # 상용의 경우엔 이 부분을 SEQUENCE 값을 조정하며 여러 번 진행하게 만듬
        # 부분 문장을 100자로 구성하는데 그러다 보니 숫자로 나눠 떨어지지 않는 경우가 발생할 경우
        # 남는 요소를 버리게 되면서 실제 그 이상의 결과를 도출해야 하는 경우 요상한 응답이 발생할 수 있음
        # (위 값 보다 더 크게 만드려면 값을 높이거나 아주 낮춰야 하는데 양쪽 모두 부작용이 있음)
        # 결론은 좋은 실험값(노가다 만세)을 써야 한다는 것

        return examplesForEpoch, characterDataSet, sequenceList

    @staticmethod
    def __splitInputTarget(chunk):
        inputText = chunk[:-1]
        targetText = chunk[1:]
        return inputText, targetText

    @staticmethod
    def __customLossFunction(labels, logits):
        return sparse_categorical_crossentropy(labels, logits, from_logits=True)

    # 이 케이스는 사실상 수동으로 RNN을 구현한 것임
    # sequenceList.map(LanguageModelRepositoryImpl.__splitInputTarget) 이 부분을 통해 입력과 타겟을 분리시킴
    # 여기서 이야기하는 입력이란 SEQUENCE_LENGTH인 100개의 문자에 해당함
    # 우리 관점에서는 사용자가 입력한 문장 혹은 단어가 될 수 있음
    # 타겟은 해당 입력 이후 배치되어야 하는 문장이나 단어 혹은 문자에 해당함 (여기서는 다음 문자임)
    def trainModel(self, sequenceList, characterList):
        dataset = sequenceList.map(LanguageModelRepositoryImpl.__splitInputTarget)
        # 같은 데이터 셋을 가지고 학습하면 학습 정확도가 떨어질 수 있기 때문에 랜덤한 batch를 사용하여
        # 상황에 적절한 문자를 구성할 수 있도록 셔플시키는 작업
        shuffledDataSet = dataset.shuffle(self.BUFFER_SIZE).batch(self.BATCH_SIZE, drop_remainder=True)

        vocabularySize = len(characterList)

        # vocabularySize는 문자 집합의 크기
        # Embedding을 사용하여 각 문자를 고정 크기의 벡터로 구성
        # 결국 vocabularySize가 입력 차원에 해당함
        # batch_input_shape는 입력 데이터의 형태를 의미합니다 (앞서 문자를 추출했을 때 64였으므로)
        # None은 문자들의 구성 자체가 가변적인 것을 의미합니다.
        # 한마디로 단어나 문장을 구성할 때 문자의 개수가 일정하지 않음을 의미하는 부분입니다.

        # LSTM은 순환 신경망의 주요 구성으로 부분 문장을 처리합니다.
        # RNN_UNITS는 결국 LSTM Layer의 개수를 의미합니다.
        # 그리고 RNN의 특징은 피드백(FeedBack) 입니다.
        # 이 피드백이란 숟가락으로 밥을 떠서 먹는 것과 같은 행위인데
        # 처음에는 숟가락을 들지 못하고, 연습을 하다 보면 숟가락을 들게 되고
        # 들더라도 밥을 입 속이 아닌 어디 이상한 데다가 넣고
        # 이것도 몇 번씩 하다보면 결국 입 속으로 숟가락을 가져가게 됩니다.
        # 이와 같이 계속 실패 속에서 경험치를 쌓으면서 목적한 바로 향하게 구성하는 작업이 피드백인데
        # 피드백 루프를 구성하기 위해 LSTM엔 return_sequences라는 옵션이 있습니다.
        # return_sequences를 True로 설정하면 부분 문장을 리턴하게 됩니다.
        # 고로 지속적으로 이것이 제대로 된 것인지 아닌지 피드백하면서 갈 수 있게 됩니다.

        # stateful 옵션의 경우엔 모델이 배치 간의 상태를 유지하도록 만듭니다.
        # recurrent_initializer에 glorot_uniform의 경우 순환 계산을 하도록 만듭니다.

        # 마지막에 Dense를 사용하여 각 입력에 대한 출력을 구성하는데
        # 결국 입력 문자에 대한 출력(타겟) 문자 확률 분포에 해당합니다.
        model = Sequential([
            Embedding(vocabularySize, self.EMBEDDING_DIM, batch_input_shape=[self.BATCH_SIZE, None]),
            LSTM(self.RNN_UNITS, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform'),
            Dense(vocabularySize)
        ])

        model.compile(optimizer='adam', loss=LanguageModelRepositoryImpl.__customLossFunction)

        checkpointDirectory = './training_checkpoint'
        checkpointPrefix = os.path.join(checkpointDirectory, "ckpt_{epoch}")
        checkpointCallback = ModelCheckpoint(filepath=checkpointPrefix, save_weights_only=True)

        model.fit(shuffledDataSet, epochs=self.EPOCHS, callbacks=[checkpointCallback])

        model.save('shakespeare_model.h5')

    def requestToReadShakespeareModel(self):
        customObjects = {'__customLossFunction': LanguageModelRepositoryImpl.__customLossFunction}
        model = load_model(self.SHAKESPEARE_MODEL_PATH, custom_objects=customObjects)

        return model

    def convertTextToTensor(self, userInputText, charToIndex):
        print("repository -> convertTextToTensor()")
        input = [charToIndex[i] for i in userInputText]
        print(f"userInputText: {userInputText}")
        inputTensor = tensorflow.expand_dims(input, 0)

        return inputTensor

    def generateText(self, loadedModel, inputTensor, indexToChar):
        print("repository -> generateText()")

        vocabularySize = len(indexToChar)

        inferenceModel = Sequential([
            Embedding(vocabularySize, self.EMBEDDING_DIM, batch_input_shape=[1, None]),
            LSTM(self.RNN_UNITS, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform'),
            Dense(vocabularySize)
        ])

        inferenceModel.build(tensorflow.TensorShape([1, None]))
        inferenceModel.set_weights(loadedModel.get_weights())
        inferenceModel.reset_states()

        generatedText = []

        for _ in range(self.GENERATION_COUNT):
            # prediction = loadedModel(inputTensor)
            predictionList = inferenceModel(inputTensor)
            # print(f"prediction: {predictionList}")

            squeezedPredictionList = tensorflow.squeeze(predictionList, 0)
            predictedId = tensorflow.random.categorical(squeezedPredictionList, num_samples=1)[-1, 0].numpy()
            inputTensor = tensorflow.expand_dims([predictedId], 0)
            generatedText.append(indexToChar[predictedId])

        return ''.join(generatedText)


