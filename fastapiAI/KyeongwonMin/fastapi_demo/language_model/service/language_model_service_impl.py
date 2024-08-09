import os.path

import requests

from language_model.repository.language_model_repository_impl import LanguageModelRepositoryImpl
from language_model.service.language_model_service import LanguageModelService


class LanguageModelServiceImpl(LanguageModelService):
    DATA_FILE_PATH = "shakespeare.txt"
    SHAKESPEARE_TEXT_URL = ("https://raw.githubusercontent.com/"
                            "karpathy/char-rnn/master/data/tinyshakespeare/input.txt")

    def __init__(self):
        self.__languageModelRepository = LanguageModelRepositoryImpl()

    def __requestToAcquireShakespeareText(self):
        if not os.path.exists(self.DATA_FILE_PATH):
            response = requests.get(self.SHAKESPEARE_TEXT_URL)
            with open(self.DATA_FILE_PATH, 'w') as file:
                file.write(response.text)

    def __readShakespeareText(self):
        with open(self.DATA_FILE_PATH, 'r') as file:
            text = file.read()

        return text

    def operateLanguageModel(self):
        self.__requestToAcquireShakespeareText()
        text = self.__readShakespeareText()
        # print(f"text: {text}")

        characterList, charToIndex, indexToChar = (
            self.__languageModelRepository.preprocessForCreateUniqueCharacter(text))
        print(f"characterList: {characterList}")
        print(f"charToIndex: {charToIndex}, length(charToIndex): {len(charToIndex)}")
        print(f"indexToChar: {indexToChar}, length(indexToChar): {len(indexToChar)}")

        textAsIndex = self.__languageModelRepository.preprocessForCreateTextIndex(text, charToIndex)
        print(f"textAsIndex: {textAsIndex}, length(textAsIndex): {len(textAsIndex)}")
        examplesForEpoch, characterDataSet, sequenceList =(
            self.__languageModelRepository.createDataSet(text, textAsIndex))

        self.__languageModelRepository.trainModel(sequenceList, characterList)

    def predictWithModelingLanguage(self, userRequestForm):
        loadedShakespeareModel = self.__languageModelRepository.requestToReadShakespeareModel()
        userInputText = userRequestForm.getWannaGetPostText()

        # TODO: 임시 방편 <- 추후 charToIndex의 경우 벡터 DB등을 사용하여 관리해야함
        #       위의 학습 진행 시 사용했던 것을 그대로 가져왔음
        text = self.__readShakespeareText()
        characterList, charToIndex, indexToChar = (
            self.__languageModelRepository.preprocessForCreateUniqueCharacter(text))

        print(f"charToIndex: {charToIndex}, length(charToIndex): {len(charToIndex)}")
        print(f"indexToChar: {indexToChar}, length(indexToChar): {len(indexToChar)}")

        inputTensor = self.__languageModelRepository.convertTextToTensor(userInputText, charToIndex)
        generatedText = self.__languageModelRepository.generateText(
            loadedShakespeareModel, inputTensor, indexToChar)

        print(f"generatedText: {generatedText}")


