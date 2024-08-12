import os

import requests

from language_model.repository.language_model_repository_impl import LanguageModelRepositoryImpl
from language_model.service.language_model_service import LanguageModelService

from tensorflow.keras.models import load_model


class LanguageModelServiceImpl(LanguageModelService):
    DATA_FILE_PATH = "shakespeare.txt"
    SHAKESPEARE_TEXT_URL = ("https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt")


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
        # print(f"text : {text}")


        characterList, charToIndex, indexToChar = self.__languageModelRepository.preprocessForCertainUniqueCharacter(text)
        textAsIndex = self.__languageModelRepository.preprocessForCertainTextIndex(text, charToIndex)
        exampleForEpoch, characterDataSet, sequenceList =(
            self.__languageModelRepository.createDataSet(text, textAsIndex))

        self.__languageModelRepository.trainModel(sequenceList, characterList)

    def predictWithModelingLanguage(self, userRequestForm):
        loadedShakespeareModel = self.__languageModelRepository.requestToReadShakespeareModel()
        userInputText = userRequestForm.getWannaGetPostText()

        # charToIndex를 얻기 위해서 위 함수에서 그래도 가져옴
        # convertTextToTensor함수에서 필요함
        text = self.__readShakespeareText()
        characterList, charToIndex, indexToChar = self.__languageModelRepository.preprocessForCertainUniqueCharacter(
            text)

        # 텍스트를 벡터로 바꿈
        inputTensor = self.__languageModelRepository.convertTextToTensor(userInputText, charToIndex)
        generatedText = self.__languageModelRepository.generateText(
            loadedShakespeareModel, inputTensor, indexToChar)

        print(f"generatedText: {generatedText}")


