from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split

from review_analysis.repository.review_analysis_repository import ReviewAnalysisRepository


class ReviewAnalysisRepositoryImpl(ReviewAnalysisRepository):
    token = Tokenizer(lower=False)

    def reviewTrain(self):
        pass

    def preprocess(self, xData, yData, englishStop):
        xRemovedHtmlTagData = xData.replace({'<.*?>': ''}, regex=True)
        xOnlyAlphabetData = xRemovedHtmlTagData.replace({'[^A-Za-z]': ''}, regex=True)

        # 사용 데이터(xOnlyAlphabetData)는 실제 pandas로 인해 DataFrame 상태에 해당함
        # apply lambda를 통해서 각 프레임의 review 들에 대해 모두 적용
        # review.split()으로 텍스트를 공백 기준으로 나누어 단어 단위로 분석함
        # 그 중 englishStop에 해당하는 불용어가 나오는 것을 제끼고 진행
        xExcludeStopData = xOnlyAlphabetData.apply(
            lambda review: [stop for stop in review.split() if stop not in englishStop])
        xMeanfulData = xExcludeStopData.apply(lambda review: [word.lower() for word in review])

        yData = yData.replace('positive', 1)
        yData = yData.replace('negative', 0)

        return xMeanfulData, yData

    def splitTrainTestSet(self, xMeanfulData, yData):
        return train_test_split(xMeanfulData, yData, test_size=0.2, random_state=42)

    def tokenize(self, xTrain, xTest, reviewMaxLength):
        self.token.fit_on_texts(xTrain)
        xTrainSequenceList = self.token.texts_to_sequences(xTrain)
        xTestSequenceList = self.token.texts_to_sequences(xTest)

        xPaddingTrainSequenceList = (
            pad_sequences(xTrainSequenceList, maxlen=reviewMaxLength, padding='post', truncating='post'))
        xPaddingTestSequenceList = (
            pad_sequences(xTestSequenceList, maxlen=reviewMaxLength, padding='post', truncating='post'))

        totalWordCount = len(self.token.word_index) + 1

        return xPaddingTrainSequenceList, xPaddingTestSequenceList, totalWordCount
