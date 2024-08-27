import numpy as np
from motor.motor_asyncio import AsyncIOMotorDatabase

from openai_basic.repository.openai_basic_repository_impl import OpenAIBasicRepositoryImpl
from openai_basic.service.openai_basic_service import OpenAIBasicService


class OpenAIBasicServiceImpl(OpenAIBasicService):
    def __init__(self, vectorDbPool: AsyncIOMotorDatabase):
        self.__openAiBasicRepository = OpenAIBasicRepositoryImpl(vectorDbPool)

    async def letsTalk(self, userSendMessage):
        return self.__openAiBasicRepository.generateText(userSendMessage)

    async def sentimentAnalysis(self, userSendMessage):
        return self.__openAiBasicRepository.sentimentAnalysis(userSendMessage)

    async def audioAnalysis(self, audioFile):
        return self.__openAiBasicRepository.audioAnalysis(audioFile)

    async def textSimilarityAnalysis(self, paperTitleList, userRequestPaperTitle):
        embeddingList = []
        embeddingCollection = self.__openAiBasicRepository.embeddingList()

        for paperTitle in paperTitleList:
            record = await embeddingCollection.find_one({"title": paperTitle})

            if record:
                embeddingList.append(np.array(record['embedding']))

            else:
                embedding = self.__openAiBasicRepository.openAiBasedEmbedding(paperTitle)

                await embeddingCollection.insert_one({"title": paperTitle, "embedding": embedding})

                embeddingList.append(np.array(embedding))

        embeddingVectorDimension = len(embeddingList)
        faissIndex = self.__openAiBasicRepository.createL2FaissIndex(embeddingVectorDimension)
        embeddingMatrix = np.array(embeddingList).astype('float32')
        faissIndex.add(embeddingMatrix)

        return self.__openAiBasicRepository.similarityAnalysis(userRequestPaperTitle, faissIndex)
