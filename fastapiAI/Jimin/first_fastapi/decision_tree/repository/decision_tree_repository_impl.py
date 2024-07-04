from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from decision_tree.repository.decision_tree_repository import DecisionTreeRepository

import pandas as pd
import tensorflow as tf
import tensorflow_decision_forests as tfdf


class DecisionTreeRepositoryImpl(DecisionTreeRepository):
    def loadWineInfo(self):
        # skleran에 들어있는 wine정보를 불러옴
        return load_wine()

    def createDataFrame(self, data, featureNames):
        df = pd.DataFrame(data=data, columns=featureNames)
        return df

    def splitTrainTestSet(self, wineDataFrame):
        return train_test_split(wineDataFrame, test_size=0.2, random_state=42)

    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        scaler = StandardScaler() # 데이터가 들쭉날쭉 하니까 정형화 시켜줌
        # 원래라면 fit 이후 transform을 해야함
        # 그러나 fit_transform은 이것을 한번에 하도록 만들어줌

        # fit은 데이터를 분석하여 내부 파라미터를 학습하게 됨
        # transform은 학습된 내부 파라미터를 사용하여 데이터를 변환합
        # 고로 transform은 fit이 반드시 먼저 선행되어야 함
        trainDataFrame[featureNames] = scaler.fit_transform(trainDataFrame[featureNames]) # 사람들이 직접 추출해줘야 하는걸 fit_transform을 쓰면 컴퓨터가 해줌
        testDataFrame[featureNames] = scaler.transform(testDataFrame[featureNames])

        return trainDataFrame, testDataFrame

    def sliceTensor(self, scaledTrainDataFrame, scaledTestDataFrame):
        # from_tensor_slices()는 pandas에서 읽은 데이터를 tensorFlow 사용 primitives로 구성하기 위해 필요한 라이브러리입니다.
        # 결론적으로 pandas 데이터 -> tensorFlow 데이터로 만들 때 사용한다고 파악하면 됩니다.
        trainDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTrainDataFrame.drop("target", axis=1)),
            scaledTrainDataFrame['target'].astype(int))
        )
        testDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTestDataFrame.drop("target", axis=1)),
             scaledTestDataFrame['target'].astype(int))
        )

        return trainDataFrameAfterSlice, testDataFrameAfterSlice

        # print(f"trainDataFrameAfterSlice: {trainDataFrameAfterSlice}")

    def applyBatchSize(self, trainDataFrameAfterSlice, testDataFrameAfterSlice, batchSize):
        readyForLearnTrainData = trainDataFrameAfterSlice.batch(batchSize) # tensor화를 시켰기 때문에 그 내장되어 있는 것으로 .batch를 썼다.
        readyForLearnTestData = testDataFrameAfterSlice.batch(batchSize)

        return readyForLearnTrainData, readyForLearnTestData

    def learn(self, readyForLearnTrainData):
        model = tfdf.keras.RandomForestModel(num_trees=100, max_depth=12, min_examples=6)
        model.fit(readyForLearnTrainData)

        return model








