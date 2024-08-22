import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from keras.src.utils import pad_sequences, to_categorical
from tensorflow.keras.preprocessing.text import Tokenizer

from sequence_analysis.repository.sequence_analysis_repository import SequenceAnalysisRepository

# 그저께: 4, 어제:5, 오늘도: 6, 내일도: 7, 모레도: 8, 이번주: 9, 이벌달: 10, 일년: 11, 10년간: 12, 100년간: 13
# 비가: 1, 왔다: 2, 내내: 14, 비가와서: 14, 잠겼다: 15 -> 빈도수가 가장 많기 때문에 '비가'가 1번

# **** 이전 버전
# extractSequence() -> inputSequences: [[5, 1], [5, 1, 3], [6, 1], [6, 1, 3], [7, 1], [7, 1, 3], [8, 1], [8, 1, 2], [9, 1], [9, 1, 2], [10, 4], [10, 4, 1], [10, 4, 1, 2], [11, 4], [11, 4, 1], [11, 4, 1, 2], [12, 4], [12, 4, 1], [12, 4, 1, 2], [13, 1], [13, 1, 3], [14, 15], [14, 15, 16]]
# paddingSequence() -> inputSequences: [[ 0  0  5  1]

# **** 현재 버전 '온다' -> '왔다'
# extractSequence() -> inputSequences: [[4], [4, 1], [4, 1, 2], [5], [5, 1], [5, 1, 2], [6], [6, 1], [6, 1, 2], [7], [7, 1], [7, 1, 2], [8], [8, 1], [8, 1, 2], [9], [9, 3], [9, 3, 1], [9, 3, 1, 2], [10], [10, 3], [10, 3, 1], [10, 3, 1, 2], [11], [11, 3], [11, 3, 1], [11, 3, 1, 2], [12], [12, 1], [12, 1, 2], [13], [13, 14], [13, 14, 15]]
# paddingSequence() -> inputSequences: [[ 0  0  0  4]

# [4, 1, 2], [5, 1, 2], [6, 1, 2], [7, 1, 2], [8, 1, 2],
# [9, 3, 1, 2], [10, 3, 1, 2], [11, 3, 1, 2], [12, 1, 2], [13, 14, 15]

# 다음으로 n-gram 시퀀스 생성을 통해 '오늘도 비가 왔다' 는 아래와 같은 구성이 가능해짐
# [4], [4, 1], [4, 1, 2]
# 그러면 자연스럽게 나머지도
# [5], [5, 1], [5, 1, 2] 형태의 구성을 가지게 됨
# 그래서 extractSequence를 보면 구성 가능한 형태들의 열거가 쭉 나열되어 있음
# 이후 padding이 진행되면서 최대 구성이 4이므로 0 값들이 필요한 숫자만큼 채워짐

# X, y를 구성할 땐 단순하게 맨 앞에 3개가 X로 배치됨
# y의 경우엔 One Hot Encoding이 진행됨

# [0 0 0 4] -> X: [0, 0, 0], y: [0, 0, 0, 0, 1, 0, ....]
# [0 0 4 1] -> X: [0, 0, 4], y: [0, 1, 0, 0, 0, 0, ....]
# [0 0 1 2] -> X: [0, 4, 1], y: [0, 0, 1, 0, 0, 0, ....]


preDefinedUserMessage = [
    "그저께 비가 왔다.",
    "어제 비가 왔다.",
    "오늘도 비가 왔다.",
    "내일도 비가 왔다.",
    "모레도 비가 왔다.",
    "이번주 내내 비가 왔다.",
    "이번달 내내 비가 왔다.",
    "일년 내내 비가 왔다.",
    "10년간 비가 왔다.",
    "100년간 비가와서 잠겼다."
]


class SequenceAnalysisRepositoryImpl(SequenceAnalysisRepository):
    def createTokenizer(self, userSendMessage):
        tokenizer = Tokenizer()
        # tokenizer.fit_on_texts(userSendMessage)
        tokenizer.fit_on_texts(preDefinedUserMessage)

        print(f"createTokenizer() -> tokenizer: {tokenizer}")
        return tokenizer

    def extractSequence(self, tokenizer, userSendMessage):
        totalWords = len(tokenizer.word_index) + 1

        inputSequences = []

        # for line in userSendMessage:
        for line in preDefinedUserMessage:
            tokenList = tokenizer.texts_to_sequences([line])[0]
            print(f"extractSequence() -> tokenList: {tokenList}")
            for index in range(1, len(tokenList)):
                nGramSequence = tokenList[:index+1]
                inputSequences.append(nGramSequence)

        print(tokenizer.word_index)
        print(f"extractSequence() -> inputSequences: {inputSequences}")
        return totalWords, inputSequences

    def paddingSequence(self, inputSequneces, maxSequenceLength):
        # maxSequenceLength = max([len(x) for x in inputSequneces])
        inputSequneces = np.array(pad_sequences(inputSequneces, maxlen=maxSequenceLength, padding='pre'))

        print(f"paddingSequence() -> inputSequences: {inputSequneces}")

        return inputSequneces

    def separateInputAndOutputSequences(self, paddedInputSequences, totalWords):
        X, y = paddedInputSequences[:,:-1], paddedInputSequences[:,-1]
        y = to_categorical(y, num_classes=totalWords)

        print(f"X: {X}, y: {y}")

        return X, y

    def trainSequence(self, totalWords, maxSequenceLength, X, y):
        model = Sequential()

        model.add(Embedding(totalWords, 128, input_length=maxSequenceLength - 1))
        model.add(LSTM(500, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(200))
        model.add(Dropout(0.2))
        model.add(Dense(totalWords, activation='softmax'))

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X, y, epochs=200, verbose=1, batch_size=64)

        return model

    def generateText(self, firstText, wannaCreateTextNumber, trainedModel, maxSequenceLength, tokenizer):
        for _ in range(wannaCreateTextNumber):
            tokenList = tokenizer.texts_to_sequences([firstText])[0]
            tokenList = pad_sequences([tokenList], maxlen=maxSequenceLength - 1, padding='pre')
            predictedList = trainedModel.predict(tokenList, verbose=0)

            predictedList = np.asarray(predictedList).astype('float64')
            predictedList = np.log(predictedList + 1e-7) / 1.0
            expPredictedList = np.exp(predictedList)
            predictedList = expPredictedList / np.sum(expPredictedList)
            probabilities = np.random.multinomial(1, predictedList[0], 1)
            predictedWordIndex = np.argmax(probabilities)

            predictedWord = tokenizer.index_word[predictedWordIndex]
            firstText += " " + predictedWord

        return firstText







