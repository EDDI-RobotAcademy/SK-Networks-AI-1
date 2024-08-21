import numpy as np

from openai_basic.controller.response_form.openai_paper_similarity_analysis_response_form import \
    OpenAIPaperSimilarityAnalysisResponseForm
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

    async def textSimilarityAnalysis(self, paperTitleList, userRequestPaperTitle):
        embeddingList = [
            self.__openAiBasicRepository.openAiBasedEmbedding(paperTitle)
            for paperTitle in paperTitleList]

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
