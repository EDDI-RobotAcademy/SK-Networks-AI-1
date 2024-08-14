from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from tf_idf_bow.repository.tf_idf_bow_repository import TfIdfBowRepository


documentTitleListForTest = [
    "자연어 처리는 인공지능의 한 분야다.",
    "인공지능은 다양한 분야에서 사용된다.",
    "자연어 처리는 텍스트 데이터를 다룬다.",
    "다양한 텍스트 데이터를 통해 자연어 처리가 발전한다.",
    "인공지능 기술은 급격히 발전하고 있다.",
    "많은 기업들이 인공지능을 활용하고 있다.",
    "축구는 인기 있는 스포츠다.",
    "치킨과 맥주의 궁합이 좋다.",
    "올림픽 경기는 4년마다 열린다.",
    "영화에 다양한 장르가 존재한다.",
    "오래전부터 군사 기술에 인공지능이 사용되어 왔다.",
    "프랑스가 올림픽에서 한국을 북한이라고 소개했다.",
    "프랑스가 올림픽에서 한국을 북한이라 소개하여 한국 네티즌들이 프랑스 국기에 나치 상징을 새겼다.",
    "나중에 또 살펴보니 프랑스가 뉴스에서 한국에 일장기를 그려넣었다.",
    "프랑스가 일장기를 그려넣은 것이 더 먼저 일어난 일이다.",
    "역시 프랑스는 유럽의 중궈다.",
]

class TfIdfBowRepositoryImpl(TfIdfBowRepository):
    TOP_RANK_LIST = 3
    SIMILARITY_THRESHOLD = 0.1

    # 여기서 TOP_RANK_LIST를 3개로 지정하여 유사도가 높은 것 중 3개를 뽑습니다.
    # 또한 제약 사항으로 THRESHOLD(임계치)를 줘서 유사도 10% 이상의 것만 추출하도록 만들었습니다.

    def findSimilar(self, message, countVectorizer, countMatrix):
        messageVector = countVectorizer.transform([message])
        # 여기서 코사인 유사도를 뽑은 리스트를 가지게 됩니다.
        cosineSimilarityList = cosine_similarity(messageVector, countMatrix).flatten()
        # 그 중 TOP RANK에 속하는 3가지만 뽑습니다.
        similarIndiceList = cosineSimilarityList.argsort()[-self.TOP_RANK_LIST:][::-1]
        # 그 중에서도 THRESHOLD 값인 최소 임계치 (10%) 이상인 녀석들만 다시 추려냅니다.
        similarDocumentList = [(documentTitleListForTest[index], cosineSimilarityList[index])
                               for index in similarIndiceList
                               if cosineSimilarityList[index] >= self.SIMILARITY_THRESHOLD]

        return similarDocumentList

    # 실질적으로 문장을 벡터화 하는 녀석입니다.
    def documentVectorization(self):
        countVectorizer = CountVectorizer()
        # 상위의 배열에 기록되어 있는 문서 제목에 해당하는 문장을 가지고 벡터화를 진행합니다.
        # 그리고 그 결과를 countMatrix에 저장합니다.
        countMatrix = countVectorizer.fit_transform(documentTitleListForTest)

        return countVectorizer, countMatrix