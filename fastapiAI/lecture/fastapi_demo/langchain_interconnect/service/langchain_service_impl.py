from langchain_interconnect.repository.langchain_repository_impl import LangchainRepositoryImpl
from langchain_interconnect.service.langchain_service import LangchainService


class LangchainServiceImpl(LangchainService):
    def __init__(self):
        self.__langchainRepository = LangchainRepositoryImpl()

    async def ragWithLangChain(self, userSendMessage):
        documentList = self.__langchainRepository.loadDocumentation()
        print(f"documentList: {documentList}")

        textChunk = self.__langchainRepository.createTextChunk(documentList)
        faissIndex = self.__langchainRepository.createFaissIndex(textChunk)

        llm = self.__langchainRepository.loadLLMChain()
        chain = self.__langchainRepository.createRagChain(llm, faissIndex)

        response = self.__langchainRepository.runChain(chain, userSendMessage)
        return response