import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from decision_tree.repository.decision_tree_repository import DecisionTreeRepository

# pip install tensorflow_decision_forests (설치 명령어)
# pip install --upgrade typing_extensions (위 명령어 실패시 설치 명렁어)
import tensorflow_decision_forests as tfdf
import tensorflow as tf
import pandas as pd


class DecisionTreeRepositoryImpl(DecisionTreeRepository):

    def loadWineInfo(self):
        return load_wine()

    def createDataFrame(self, data, featureNames):
        df = pd.DataFrame(data=data, columns=featureNames)
        return df

    def splitTrainTestSet(self, wineDataFrame):
        return train_test_split(wineDataFrame, test_size=0.2, random_state=42)

    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        scaler = StandardScaler()
        trainDataFrame[featureNames] = scaler.fit_transform(trainDataFrame[featureNames])
        testDataFrame[featureNames] = scaler.fit_transform(testDataFrame[featureNames])

        return trainDataFrame, testDataFrame

    def sliceTensor(self, scaledTrainDataFrame, scaledTestDataFrame):
        trainDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTrainDataFrame.drop("target", axis=1)),
            scaledTrainDataFrame['target'].astype(int))
        )
        testDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTestDataFrame.drop("target", axis=1)),
             scaledTestDataFrame['target'].astype(int))
        )
        # print(f"trainDataFrameAfterSlice: {trainDataFrameAfterSlice}")

        return trainDataFrameAfterSlice, testDataFrameAfterSlice

    def applyBatchSize(self, trainDataFrameAfterSlice, testDataFrameAfterSlice, batchSize):
        readyForLearnTrainData = trainDataFrameAfterSlice.batch(batchSize)
        readyForLearnTestData = testDataFrameAfterSlice.batch(batchSize)

        return readyForLearnTrainData, readyForLearnTestData

    def learn(self, readyForLearnTrainData):
        model = tfdf.keras.RandomForestModel(num_trees=100, max_depth=12, min_examples=6)
        model.fit(readyForLearnTrainData)

        return model