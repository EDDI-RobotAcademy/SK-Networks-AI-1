import numpy as np

from openai_basic.controller.response_form.openai_paper_similarity_analysis_response_form import \
    OpenAIPaperSimilarityAnalysisResponseForm
from openai_basic.repository.openai_basic_repository_impl import OpenAIBasicRepositoryImpl
from openai_basic.service.openai_basic_service import OpenAIBasicService
from motor.motor_asyncio import AsyncIOMotorDatabase


class OpenAIBasicServiceImpl(OpenAIBasicService):
    def __init__(self, vectorDbPool: AsyncIOMotorDatabase):
        self.__openAiBasicRepository = OpenAIBasicRepositoryImpl(vectorDbPool)

    async def letsTalk(self, userSendMessage):
        return await self.__openAiBasicRepository.generateText(userSendMessage)

    async def sentimentAnalysis(self, userSendMessage):
        return self.__openAiBasicRepository.sentimentAnalysis(userSendMessage)

    async def audioAnalysis(self, audioFile):
        return self.__openAiBasicRepository.audioAnalysis(audioFile)

    async def textSimilarityAnalysis(self, paperTitleList, userRequestPaperTitle):
        embeddingList = []
        embeddingCollection = self.__openAiBasicRepository.embeddingList()

        for paperTitle in paperTitleList:
            # MongoDB에서 임베딩을 찾는다
            record = await embeddingCollection.find_one({"title": paperTitle})

            if record:
                # MongoDB에 임베딩이 존재하는 경우
                embeddingList.append(np.array(record['embedding']))
            else:
                # 임베딩이 존재하지 않는 경우 OpenAI API를 호출하여 임베딩 생성
                embedding = self.__openAiBasicRepository.openAiBasedEmbedding(paperTitle)

                # MongoDB에 새 임베딩을 저장
                await embeddingCollection.insert_one({"title": paperTitle, "embedding": embedding})

                embeddingList.append(np.array(embedding))

        # embeddingList = [
        #     self.__openAiBasicRepository.openAiBasedEmbedding(paperTitle)
        #     for paperTitle in paperTitleList]

        embeddingVectorDimension = len(embeddingList[0])
        faissIndex = self.__openAiBasicRepository.createL2FaissIndex(embeddingVectorDimension)
        embeddingMatrix = np.array(embeddingList).astype('float32')
        faissIndex.add(embeddingMatrix)

        indexList, distanceList = (
            self.__openAiBasicRepository.similarityAnalysis(userRequestPaperTitle, faissIndex))

        print(f"indexList: {indexList}, distanceList: {distanceList}")

        return OpenAIPaperSimilarityAnalysisResponseForm.fromOpenAIPaperSimilarityAnalysis(
            indexList, distanceList, paperTitleList
        )
