import numpy as np
import tensorflow

from language_model.repository.language_model_repository import LanguageModelRepository


class LanguageModelRepositoryImpl(LanguageModelRepository):
    SEQUENCE_LENGTH = 100

    # 고유 문자 목록 생성
    def preprocessForCreateUniqueCharacter(self, text):
        characterList = sorted(list(set(text)))
        charToIndex = {character: index for index, character in enumerate(characterList)}
        indexToChar = np.array(characterList)

        return charToIndex, indexToChar

    def preprocessForCreateTextIndex(self, text, charToIndex):
        return np.array([charToIndex[character] for character in text])

    def createDataSet(self, text, textAsIndex):
        examplesForEpoch = len(text) // self.SEQUENCE_LENGTH
        characterDataSet = tensorflow.data.Dataset.from_tensor_slices(textAsIndex)
        sequenceList = characterDataSet.batch(self.SEQUENCE_LENGTH + 1, drop_remainder=True)

        return examplesForEpoch, characterDataSet, sequenceList
    