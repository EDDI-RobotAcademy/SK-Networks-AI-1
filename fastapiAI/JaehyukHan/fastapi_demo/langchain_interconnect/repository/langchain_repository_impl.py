from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI

from langchain_interconnect.repository.langchain_repository import LangchainRepository
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


class LangchainRepositoryImpl(LangchainRepository):
    DOCUMENT_FILE = 'documents.txt'

    def __init__(self):
        self.chatHistory = []

    def loadDocumentation(self):
        with open(self.DOCUMENT_FILE, "r") as file:
            text = file.read()

        return text

    def createTextChunk(self, documentList, chunk_size=1000, chunk_overlap=0):
        chunks = []
        start = 0
        while start < len(documentList):
            end = min(start + chunk_size, len(documentList))
            chunks.append(documentList[start:end])
            start += chunk_size - chunk_overlap
        return chunks

    def createFaissIndex(self, documentList):
        embeddings = OpenAIEmbeddings()
        return FAISS.from_texts(documentList, embeddings)

    def loadLLMChain(self):
        return ChatOpenAI(model_name="gpt-4")

    def createRagChain(self, llm, faissIndex):
        return ConversationalRetrievalChain.from_llm(llm, retriever=faissIndex.as_retriever())

    def runChain(self, chain, userSendMessage):
        response = chain.run({"question": userSendMessage, "chat_history": self.chatHistory})
        self.chatHistory.append({"question": userSendMessage, "answer": response})

        return response