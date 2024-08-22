from openai_basic.repository.openai_basic_repository_impl import OpenAIBasicRepositoryImpl
from openai_basic.service.openai_basic_service import OpenAIBasicService


class OpenAIBasicServiceImpl(OpenAIBasicService):
    def __init__(self):
        self.__openAiBasicRepository = OpenAIBasicRepositoryImpl()

    async def letsTalk(self, userSendMessage):
        return await self.__openAiBasicRepository.generateText(userSendMessage)

    async def sentimentAnalysis(self, userSendMessage):
        return self.__openAiBasicRepository.sentimentAnalysis(userSendMessage)
    
    async def audioAnalysis(self, audioFile):
        return self.__openAiBasicRepository.audioAnalysis(audioFile)

    async def textSimilarityAnalysis(self, paperTitleList):
        embeddingList = [
            self.__openAiBasicRepository.openAiBasedEmbedding(paperTitle)
            for paperTitle in paperTitleList]
        # self.__openAiBasicRepository.openAiBasedEmbedding(paperTitleList)

        # return self.__openAiBasicRepository.similarityAnalysis(userSendMessage)