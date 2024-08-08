from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from tf_idf_bow.repository.tf_idf_bow_repository_impl import TfIdfBowRepository

documentTitleListForTest = [
    '자연어 처리는 인공지능의 한 분야다.',
    '인공지능은 다양한 분야에서 사용된다.',
    '자연어 처리는 텍스트 데이터를 다룬다.',
    '다양한 텍스트 데이터를 통해 자연어 처리가 발전한다.',
    '인공지능 기술은 급격히 발전하고 있다.',
    '많은 기업들이 인공지능을 활용하고 있다.',
    '축구는 인기 있는 스포츠다.',
    '치킨과 맥주의 궁합이 좋다.',
    '올림픽 경기는 4년마다 열린다.',
    '영화에 다양한 장르가 존재한다.',
    '오래전부터 군사 기술에 인공지능이 사용되어왔다.',
    '프랑스가 올림픽에서 한국을 북한이라고 소개했다.',
    '프랑스가 올림픽에서 한국을 북한이라 소개하여 한국 네티즌들이 프랑스 국기에 나치 상징을 새겼다.',
    '나중에 또 살펴보니 프랑스가 뉴스에서 한국에 일장기를 그려넣었다.',
    '프랑스가 일장기를 그려넣은 것이 더 먼저 일어난 일이다.',
    '역시 프랑스는 유럽의 중국이다.',
]

class TfIdfBowRepositoryImpl(TfIdfBowRepository):
    TOP_RANK_LIST = 3
    SIMILARITY_THRESHOLD = 0.1

    def findSimlar(self, message, countVectorizer, countMatrix):
        messageVector = countVectorizer.transform([message])
        cosineSimilarityList = cosine_similarity(messageVector, countMatrix).flatten()
        similarIndiceList = cosineSimilarityList.argsort()[-self.TOP_RANK_LIST:][::-1]
        similarDocumentList = [(documentTitleListForTest[index], cosineSimilarityList[index])
                               for index in similarIndiceList if cosineSimilarityList[index] >= self.SIMILARITY_THRESHOLD]

        return similarDocumentList

    def documentVectorization(self):
        countVectorizer = CountVectorizer()
        countMatrix = countVectorizer.fit_transform(documentTitleListForTest)

        return countVectorizer, countMatrix