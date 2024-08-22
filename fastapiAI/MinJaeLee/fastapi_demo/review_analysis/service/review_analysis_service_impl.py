import os
from typing import re

import numpy as np
import pandas as pd
from keras.src.legacy.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
from tensorflow.python.keras.saving.saved_model import load

from review_analysis.repository.review_analysis_repository_impl import ReviewAnalysisRepositoryImpl
from review_analysis.service.review_analysis_service import ReviewAnalysisService


class ReviewAnalysisServiceImpl(ReviewAnalysisService):
    REVIEW_CSV_FILE_PATH = "../assets/IMDB Dataset.csv"
    REVIEW_MODEL_FILE_PATH = ""
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
        xTrain, xTest, yTrain, yTest = (self.__reviewAnalysisRepository.splitTrainTestSet(xMeanfulData, yData))

        reviewMaxLength = self.__calculateReviewMaxLength(xTrain)
        #
        # tokenizer = Tokenizer(lower=False)
        # tokenizeWordList = tokenizer.texts_to_sequences([preprocessedTextList])
        # tokenziedPaddingWordList = pad_sequences(tokenizeWordList, maxlen = reviewMaxLength, padding='post', truncating='post')
        #
        # result = loadedReviewModel.predict(tokenziedPaddingWordList)

        xPaddingTrainSequenceList, xPaddingTestSequenceList, totalWordCount = (
            self.__reviewAnalysisRepository.tokenize(xTrain, xTest, reviewMaxLength))

        self.__reviewAnalysisRepository.createModel(totalWordCount, reviewMaxLength, xPaddingTrainSequenceList, yTrain)

        # return "Learning Process Complete"

    def __loadReviewTrainedModel(self):
        return load.model(self.REVIEW_MODEL_FILE_PATH)

    def __createMeanfulTextList(self, userInputText):
        removeHtmlTagTextList = re.sub(r'<.*?>', '', userInputText)
        onlyAlphabetTextList = re.sub(r'[^A-Za-z\s]', '', removeHtmlTagTextList)

        wordList = onlyAlphabetTextList.split(' ')
        filteredWordList = [word for word in wordList not in self.englishStop]

        return ''.join(filteredWordList).lower()

    def sentimentAnalysis(self, userReviewRequestForm):
        loadedModel = self.__loadReviewTrainedModel()
        userInputText = userReviewRequestForm.getUserInputText()

        preprocessedText = self.__createMeanfulTextList(userInputText)
        print(f"preprocessedTextList: {preprocessedText}")
