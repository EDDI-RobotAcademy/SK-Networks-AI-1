import numpy as np
import tensorflow as tf
from keras import Sequential
from keras.src.layers import LSTM, Embedding, Dropout, Dense
from keras.src.utils import pad_sequences, to_categorical
from tensorflow.keras.preprocessing.text import Tokenizer

from sequence_analysis.repository.sequence_analysis_repository import SequenceAnalysisRepository

# 그저께: 1, 비가: 2, 왔다: 3
# 어제: 4, 오늘도: 5 내일도: 6
# 모레도: 7, 이번주: 8, 내내: 9
# 이번달: 10, 일년: 11, 10년간: 12
# 100년간: 13, 비가와서:14, 잠겼다: 15

# 다음으로 n-gram 시퀀스 생성을 통해 '오늘도 비가 왔다' 는 아래와 같은 구성이 가능
# [4], [4, 1], [4, 1, 2]
# 그러면 자연스럽게 나머지도 같은 형태의 구성을 가지게 됨
# 그래서 extractSequence를 보면 구성 가능한 형태들의 열거가 쭉 나열되어 있음
# 이후 padding 이 진행되면서 최대 구성이 4

# X, y를 구성 할 땐 단순하게
# 맨 앞에 3개가 X로 배치됨
# y의 경우엔 One Hot Encoding이 진행됨
preDefinedUserMessage = [
    "그저께 비가 왔다.",
    "어제 비가 왔다.",
    "오늘도 비가 왔다.",
    "내일도 비가 왔다.",
    "모래도 비가 왔다.",
    "이번주 내내 비가 왔다.",
    "이번달 내내 비가 왔다.",
    "일년 내내 비가 왔다.",
    "10년간 비가 왔다.",
    "199년간 비가와서 잠겼다",
]


class SequenceAnalysisRepositoryImpl(SequenceAnalysisRepository):
    def createTokenizer(self, userSendMessage):
        print(f"repository -> tokenize()")
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(preDefinedUserMessage)

        return tokenizer

    def extractSequence(self, tokenizer, userSendMessage):
        print(f"repository -> extractSequence()")

        totalWords = len(tokenizer.word_index) + 1

        inputSequences = []
        for line in preDefinedUserMessage:
            tokenList = tokenizer.texts_to_sequences([line])[0]
            print(tokenList)
            for i in range(1, len(tokenList)):
                nGramSequence = tokenList[:i + 1]
                inputSequences.append(nGramSequence)
        print(f"inputSequence: {inputSequences}")
        return totalWords, inputSequences

    def paddingSequence(self, inputSequences, maxSequenceLength):
        inputSequences = np.array(pad_sequences(inputSequences, maxlen=maxSequenceLength, padding='pre'))
        print("paddedSequences:", inputSequences)
        return inputSequences

    def separateInputAndOutputSequences(self, paddedInputSequences, totalWord):
        X, y = paddedInputSequences[:, :-1], paddedInputSequences[:, -1]
        y = to_categorical(y, num_classes=totalWord)

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
