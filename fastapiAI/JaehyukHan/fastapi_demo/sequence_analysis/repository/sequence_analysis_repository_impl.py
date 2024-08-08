import numpy as np
import tensorflow as tf
from keras.utils import to_categorical
from keras_preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

from sequence_analysis.repository.sequence_analysis_repository import SeqeunceAnalysisRepository

# gpus = tf.config.list_physical_devices('GPU')
# tf.config.set_visible_devices(gpus[0], 'GPU')

# '비가': 1, '왔다': 2, '내내': 3,
# '그저께': 4, '어제': 5, '오늘도': 6,
# '내일도': 7, '모레도': 8, '이번주': 9,
# '이번달': 10, '일년': 11, '10년간': 12,
# '100년간': 13, '비가와서': 14, '잠겼다': 15

# n-gram 시퀀스 생성을 통해 '오늘도 비가 왔다' 는 아래와 같은 구성이 가능해짐
# [5, 2], [5, 2, 3]
# 그러면 자연스럽게 나머지도
# [5], [5, 1], [5, 1, 2] 형태의 구성을 가지게 됨
# 그래서 extractSequence를 보면 구성 가능한 형태들의 열거가 쭉 나열되어 있음
# 이후 padding이 진행되면서 최대 구성이 4이므로 0 값들이 필요한 개수만큼 채워짐

# X, y를 구성할 땐 단순하게
# 맨 앞의 3개가 X로 배치됨
# y의 경우엔 One-hot Encoding이 진행됨

# [0 0 0 4] -> X: [0 0 0], y: [0 0 0 0 1 0 ...]
# [0 0 4 1] -> X: [0 0 4], y: [0 1 0 0 0 0 ...]
# [0 4 1 2] -> X: [0 4 1], y: [0 0 1 0 0 0 ...]

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
    "100년간 비가와서 잠겼다.",
]

class SequenceAnalysisRepositoryImpl(SeqeunceAnalysisRepository):
    def createTokenize(self, userSendMessage):
        print(f"repository -> createTokenize() userSendMessage: {userSendMessage}")
        tokenizer = Tokenizer()
        # tokenizer.fit_on_texts(userSendMessage)
        tokenizer.fit_on_texts(preDefinedUserMessage)

        return tokenizer

    def extractSequence(self, tokenizer, userSendMessage):
        print(f"repository -> extractSequence() userSendMessage: {userSendMessage}")
        totalWords = len(tokenizer.word_index) + 1

        inputSequences = []

        # for line in userSendMessage
        for line in preDefinedUserMessage:
            tokenList = tokenizer.texts_to_sequences([line])[0]
            for index in range(1, len(tokenList)):
                nGramSequence = tokenList[:index+1]
                inputSequences.append(nGramSequence)
                # print(f"inputSequences: {inputSequences}")

        return totalWords, inputSequences

    def paddingSequence(self, inputSequences, maxSequenceLength):
        inputSequences = np.array(pad_sequences(inputSequences, maxlen=maxSequenceLength, padding='pre'))

        # print(f"paddingSequence() -> inputSequences: {inputSequences}")
        return inputSequences

    def separateInputAndOutputSequences(self, paddedInputSequences, totalWords):
        X, y = paddedInputSequences[:, :-1], paddedInputSequences[:, -1]
        y = to_categorical(y, num_classes=totalWords)

        print(f"X: {X}, y: {y}")

        return X, y

    def trainSequence(self, totalWords, maxSequenceLength, X, y):
        model = Sequential()

        model.add(Embedding(totalWords, 128, input_length=maxSequenceLength-1))
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
            tokenList = pad_sequences([tokenList], maxlen=maxSequenceLength-1, padding='pre')
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
