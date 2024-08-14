import os

import numpy as np
import pandas as pd
from nltk.corpus import stopwords

from review_analysis.repository.review_analysis_repository_impl import ReviewAnalysisRepositoryImpl
from review_analysis.service.review_analysis_service import ReviewAnalysisService


class ReviewAnalysisServiceImpl(ReviewAnalysisService):
    REVIEW_CSV_FILE_PATH = 'IMDB Dataset.csv'
    englishStop = set(stopwords.words('english'))
    def __init__(self):
        self.__reviewAnalysisRepository = ReviewAnalysisRepositoryImpl()

    def __readCsvFile(self):
        currentDirectory = os.getcwd()
        filePath = os.path.join(currentDirectory, '..', 'assets', self.REVIEW_CSV_FILE_PATH)

        dataFrame = pd.read_csv(filePath)

        return dataFrame

    def __calculateReviewMaxLength(self, xTrain):
        reviewLength = [len(review) for review in xTrain]
        return int(np.ceil(np.mean(reviewLength)))

    def reviewAnalysis(self):
        reviewDataFrame = self.__readCsvFile()

        xData = reviewDataFrame['review']
        yData = reviewDataFrame['sentiment']

        xMeanfulData, yData = self.__reviewAnalysisRepository.preprocess(xData, yData, self.englishStop)
        xTrain, xTest, yTrain, yTest = (
            self.__reviewAnalysisRepository.splitTrainTestSet(xMeanfulData, yData))

        reviewMaxLength = self.__calculateReviewMaxLength(xTrain)
        xPaddingTrainSequenceList, xPaddingTestSequenceList, totalWordCount = (
            self.__reviewAnalysisRepository.tokenize(xTrain, xTest, reviewMaxLength))

        self.__reviewAnalysisRepository.createModel(
            totalWordCount, reviewMaxLength, xPaddingTrainSequenceList, yTrain)

        return "학습이 완료되었습니다."


