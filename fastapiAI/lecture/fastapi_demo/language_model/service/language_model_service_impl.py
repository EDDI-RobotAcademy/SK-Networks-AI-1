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

        charToIndex, indexToChar = self.__languageModelRepository.preprocessForCreateUniqueCharacter(text)
        textAsIndex = self.__languageModelRepository.preprocessForCreateTextIndex(text, charToIndex)
        self.__languageModelRepository.createDataSet(text, textAsIndex)