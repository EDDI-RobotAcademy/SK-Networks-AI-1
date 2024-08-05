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
    "오래전부터 군사 기술에 인공지능이 사용되어왔다.",
    "프랑스가 올림픽에서 한국을 북한이라고 소개했다.",
    "프랑스가 올림픽에서 한국을 북한이라 소개하여 한국 네티즌들이 프랑스 국기에 나치 상징을 새겼다.",
    "나중에 또 살펴보니 프랑스가 뉴스에서 한국에 일장기를 그려넣었다.",
    "프랑스가 일장기를 그려넣은 것이 더 먼저 일어난 일이다.",
    "역시 프랑스는 유럽의 중궈다."
]

class TfIdfBowRepositoryImpl(TfIdfBowRepository):
    # 여기서 Top rank list를 3개로 지정하여 유사도가 높은 것중 3개를 뽑습니다.
    # 또한 제약 사항으로 임계값을 줘서 유사도 10% 이상의 것만 추출하도록 만들었습니다.
    TOP_RANK_LIST = 3
    SIMILARITY_THRESHOLD = 0.1

    # 기존 문서들 벡터화 (입력 제외)
    def documentVectorization(self):
        # 이걸 통해 알아서 벡터화가 됨
        countVectorizer = CountVectorizer()
        # 기존 문서(documentTitleListForTest)들을 여기에 넣음
        # 상위의 배열에 기록되어 있는 문서 제목에 해당하는 문장을 가지고 벡터화를 진행
        # 그리고 그 결과를 countMatrix에 저장함
        countMatrix = countVectorizer.fit_transform(documentTitleListForTest)

        return countVectorizer, countMatrix

    def findSimilar(self, userSendMessage, countVectorizer, countMatrix):
        # 여기 코드 제대로 이해해보기 (print 찍어보기)

        # 입력 message -> vector화
        messageVector = countVectorizer.transform([userSendMessage])
        # 입력인 메세지 벡터와 기존 문서 벡터들 사이의 cosine 유사도를 구함
        # 여기서 코사인 유사도를 뽑은 리스트를 가지게 됩니다.
        cosineSimilarityList = cosine_similarity(messageVector, countMatrix).flatten()
        # 상위 3개의 cosine 유사도를 가진 index들을 가져오기 >> 이 부분 왜 이렇게 구현했는지 찍어보기
        similarIndiceList = cosineSimilarityList.argsort()[-self.TOP_RANK_LIST:][::-1]

        # 상위 3개 index들에 대한 정보 중에서도 유사도 threshold를 넘긴 값만 추려낸다.
        # (similarDocument 에는 해당 index의 메세지와 코사인 유사도 정보가 담김)
        similarDocument = [(documentTitleListForTest[index], cosineSimilarityList[index])
                           for index in similarIndiceList
                           if cosineSimilarityList[index] >= self.SIMILARITY_THRESHOLD]
        return similarDocument