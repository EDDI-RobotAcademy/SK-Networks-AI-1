import os
import re

import numpy as np
from nltk.corpus import stopwords
from keras.models import load_model

from review_analysis.repository.review_analysis_repository_impl import ReviewAnalysisRepositoryImpl
from review_analysis.service.review_analysis_service import ReviewAnalysisService

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import pandas as pd


class ReviewAnalysisServiceImpl(ReviewAnalysisService):
    REVIEW_CSV_FILE_PATH = "IMDB Dataset.csv"
    REVIEW_MODEL_FILE_PATH = "review_analysis.h5"

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
        xPaddingTrainSequenceList, xPaddingTestSequenceList, totalWordCount =(
            self.__reviewAnalysisRepository.tokenize(xTrain, xTest, reviewMaxLength))

        self.__reviewAnalysisRepository.createModel(
            totalWordCount, reviewMaxLength, xPaddingTrainSequenceList, yTrain)

    def __loadReviewTrainedModel(self):
        return load_model(self.REVIEW_MODEL_FILE_PATH)

    def __createMeanfulTextList(self, userInputText):
        removeHtmlTagTextList = re.sub(r'<.*?>', '', userInputText)
        onlyAlphabetTextList = re.sub(r'[^A-Za-z\s]', '', removeHtmlTagTextList)

        wordList = onlyAlphabetTextList.split(' ')
        filteredWordList = [word for word in wordList if word not in self.englishStop]

        return ' '.join(filteredWordList).lower()

    def sentimentAnalysis(self, userReviewRequestForm):
        loadedReviewModel = self.__loadReviewTrainedModel()
        userInputText = userReviewRequestForm.getUserInputText()

        preprocessedTextList = self.__createMeanfulTextList(userInputText)
        print(f"preprocessedTextList: {preprocessedTextList}")

        # TODO: pickle로 저장해놓고 불렀어야함
        reviewDataFrame = self.__readCsvFile()

        xData = reviewDataFrame['review']
        yData = reviewDataFrame['sentiment']

        xMeanfulData, yData = self.__reviewAnalysisRepository.preprocess(xData, yData, self.englishStop)
        xTrain, xTest, yTrain, yTest = (
            self.__reviewAnalysisRepository.splitTrainTestSet(xMeanfulData, yData))

        reviewMaxLength = self.__calculateReviewMaxLength(xTrain)
        # TODO: pickle 처리하면 이 부분 제거하고 pickle load

        tokenizer = Tokenizer(lower=False)
        tokenizedWordList = tokenizer.texts_to_sequences([preprocessedTextList])
        tokenizedPaddingWordList = pad_sequences(
            tokenizedWordList, maxlen=reviewMaxLength, padding='post', truncating='post')
        
        result = loadedReviewModel.predict(tokenizedPaddingWordList)
        print(f"result: {result}")

        sentiment = "긍정" if result >= 0.8 else "부정"

        return sentiment
