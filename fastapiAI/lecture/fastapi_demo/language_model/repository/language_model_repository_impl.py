import os

import numpy as np
import tensorflow

from keras import Sequential
from keras.src.callbacks import ModelCheckpoint
from keras.src.layers import Embedding, LSTM, Dense
from keras.src.losses import sparse_categorical_crossentropy

from tensorflow.keras.models import load_model
from tensorflow.keras.utils import custom_object_scope

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
    def preprocessForCreateUniqueCharacter(self, text):
        characterList = sorted(list(set(text)))
        charToIndex = {character: index for index, character in enumerate(characterList)}
        indexToChar = np.array(characterList)

        return characterList, charToIndex, indexToChar

    def preprocessForCreateTextIndex(self, text, charToIndex):
        return np.array([charToIndex[character] for character in text])

    def createDataSet(self, text, textAsIndex):
        examplesForEpoch = len(text) // self.SEQUENCE_LENGTH
        characterDataSet = tensorflow.data.Dataset.from_tensor_slices(textAsIndex)
        sequenceList = characterDataSet.batch(self.SEQUENCE_LENGTH + 1, drop_remainder=True)

        return examplesForEpoch, characterDataSet, sequenceList

    @staticmethod
    def __splitInputTarget(chunk):
        inputText = chunk[:-1]
        targetText = chunk[1:]
        return inputText, targetText

    @staticmethod
    def __customLossFunction(labels, logits):
        return sparse_categorical_crossentropy(labels, logits, from_logits=True)

    def trainModel(self, sequenceList, characterList):
        dataset = sequenceList.map(LanguageModelRepositoryImpl.__splitInputTarget)
        shuffledDataset = dataset.shuffle(self.BUFFER_SIZE).batch(self.BATCH_SIZE, drop_remainder=True)

        vocabularySize = len(characterList)

        model = Sequential([
            Embedding(vocabularySize, self.EMBEDDING_DIM, batch_input_shape=[self.BATCH_SIZE, None]),
            LSTM(self.RNN_UNITS, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform'),
            Dense(vocabularySize)
        ])

        model.compile(optimizer='adam', loss=LanguageModelRepositoryImpl.__customLossFunction)

        print(f"model: {model}")

        # checkpointDirectory = './training_checkpoint'
        # checkpointPrefix = os.path.join(checkpointDirectory, "ckpt_{epoch}")
        # checkpointCallback = ModelCheckpoint(filepath=checkpointPrefix, save_weights_only=True)
        #
        # model.fit(shuffledDataset, epochs=self.EPOCHS, callbacks=[checkpointCallback])
        #
        # model.save('shakespeare_model.h5')

    def requestToReadShakespeareModel(self):
        customObjects = {'__customLossFunction': LanguageModelRepositoryImpl.__customLossFunction}

        model = load_model(self.SHAKESPEARE_MODEL_PATH, custom_objects=customObjects)
        return model

    def convertTextToTensor(self, userInputText, charToIndex):
        print("repository -> convertTextToTensor()")
        input = [charToIndex[i] for i in userInputText]
        print(f"userInputText: {userInputText}")
        print(f"input: {input}")
        inputTensor = tensorflow.expand_dims(input, 0)
        print(f"inputTensor: {inputTensor}")

        return inputTensor

    def generateText(self, loadedModel, inputTensor, indexToChar):
        print("repository -> generateText()")

        # loadedModel.layers[1].stateful = False
        # loadedModel.reset_states()

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