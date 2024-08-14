import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from keras.src.utils import pad_sequences, to_categorical
from tensorflow.keras.preprocessing.text import Tokenizer

from sequence_analysis.repository.sequence_analysis_repository import SequenceAnalysisRepository

# 그저께: 4, 어제: 5, 오늘도: 6, 내일도: 7, 모레도: 8, 이번주: 9, 이번달: 10, 일년: 11, 10년간: 12, 100년간: 13
# 비가: 1, 왔다: 2, 내내: 3, 비가와서: 14, 잠겼다: 15

preDefinedUserMessage = [
    "그저께 비가 왔다.",
    "어제 비가 왔다.",
    "오늘도 비가 왔다.",
    "내일도 비가 온다.",
    "모레도 비가 온다.",
    "이번주 내내 비가 온다.",
    "이번달 내내 비가 온다.",
    "일년 내내 비가 온다.",
    "10년간 비가 왔다.",
    "100년간 비가 와서 잠겼다."
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

        for line in preDefinedUserMessage:
            tokenList = tokenizer.texts_to_sequences([line])[0]
            for index in range(1, len(tokenList)):
                nGramSequence = tokenList[:index+1]
                inputSequences.append(nGramSequence)
                print(f"inputSequences: {inputSequences}")

        return totalWords, inputSequences

    def paddingSequence(self, inputSequences, maxSequenceLength):
        inputSequences = np.array(pad_sequences(inputSequences, maxlen=maxSequenceLength, padding='pre'))

        print(f"paddingSequence() -> inputSequences: {inputSequences}")

        return inputSequences

    def separateInputAndOutputSequences(self, paddedInputSequences, totalWords):
        X, y = paddedInputSequences[:, :-1], paddedInputSequences[:, -1]
        y = to_categorical(y, num_classes=totalWords)

        print(f"X: {X}, y: {y}")

        return X, y

    def trainSequence(self, totalWords, maxSequenceLength, X, y):
        model = Sequential()

        model.add(Embedding(totalWords, 128, input_length=maxSequenceLength - 1))
        model.add(LSTM(500, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(100))
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






