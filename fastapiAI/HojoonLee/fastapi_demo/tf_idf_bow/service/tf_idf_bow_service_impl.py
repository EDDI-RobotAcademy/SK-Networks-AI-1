from tf_idf_bow.repository.tf_idf_bow_repository_impl import TfIdfBowRepositoryImpl
from tf_idf_bow.service.tf_idf_bow_service import TfIdfBowService

class TfIdfBowServiceImpl(TfIdfBowService):
    def __init__(self):
        self.tfIdfBowRepository = TfIdfBowRepositoryImpl()

    def findSimilarDocumentList(self, userSendMessage):
        # 문서 벡터화 -> 유사도를 따지기 위해 벡터화 시킴
        countVectorizer, countMatrix = self.tfIdfBowRepository.documentVectorization()
        # 벡터화된 정보를 통해 유사도를 계산
        similarDocumentList = self.tfIdfBowRepository.findSimilar(userSendMessage, countVectorizer, countMatrix)
        response = [
            {"document": document, "similarity": score } for document, score in similarDocumentList
        ]

        return response