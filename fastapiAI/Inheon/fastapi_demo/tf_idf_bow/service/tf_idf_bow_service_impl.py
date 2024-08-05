from tf_idf_bow.service.tf_idf_bow_service import TfIdfBowService


class TfIdfBowServiceImpl(TfIdfBowService):
    def __init__(self):
        self.ifIdfBowRepository = TfIdfBowServiceImpl()

    def findSimilarDocumentList(self, userSendMessage):
        countVectorizer, countMatrix = self.tfIdfBowRepository.documentVectorization()
        similarDocumentList = self.tfIdfBowRepository.findSimilar(userSendMessage, countVectorizer, countMatrix)
        response = [
            {'document': document, 'similarity': score} for document, score in similarDocumentList
        ]

        return response