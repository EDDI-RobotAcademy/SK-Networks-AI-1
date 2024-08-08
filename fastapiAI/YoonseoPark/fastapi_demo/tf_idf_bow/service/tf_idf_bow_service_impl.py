from tf_idf_bow.repository.tf_idf_repository_impl import TfIdfBowRepositoryImpl
from tf_idf_bow.service.tf_idf_bow_service import TfIdfBowService


class TfIdfBowServiceImpl(TfIdfBowService):
    def __init__(self):
        self.tfIdfBowRepository = TfIdfBowRepositoryImpl()

    def findSimilarDocumentList(self, userSendMessage):
        countVetorizer, countMatrix = self.tfIdfBowRepository.documentVectorization()
        similarDocumentList = self.tfIdfBowRepository.findSimilar(userSendMessage, countVetorizer, countMatrix)
        response = [
            { "document": document, "similarity": score } for document, score in similarDocumentList
        ]

        return response



