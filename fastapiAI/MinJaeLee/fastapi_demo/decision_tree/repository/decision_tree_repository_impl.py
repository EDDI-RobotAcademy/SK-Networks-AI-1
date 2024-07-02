from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from decision_tree.repository.decision_tree_repsitory import DecisionTreeRepository
import pandas as pd
import tensorflow as tf
# pip install tensorflow_decision_forests
# 에러 발생시
    # pip install --upgrade typing_extensions
import tensorflow_decision_forests as tfdf


class DecisionTreeRepositoryImpl(DecisionTreeRepository):
    def loadWineInfo(self):
        print(f"loading wine data...")
        return load_wine()

    def createDataFrame(self, data, featureNames):
        print(f"create dataframe")
        df = pd.DataFrame(data=data, columns=featureNames)
        return df

    def splitTrainTestSet(self, wineDataFrame):
        return train_test_split(wineDataFrame, test_size=0.2, random_state=42)

    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        scaler = StandardScaler()

        # 원래라면 fit이후 transform 을 해야함
        # 그러나 fit_transform 은 이것을 한번에 하도록 해줌
        # (사실 Domain관점에선 좀 문제가 있으나, 제공해주는 라이브러리이므로 그냥 사용)

        # fit은 데이터를 분석하여 내부 파라미터를 학습하게 됨
        # transform 은 학습된 내부 파라미터를 사요하여 데이터를 변환함
        # 따라서 transform은 fit이 반드시 먼저 선행되어야 함
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

        print(f"trainDataFrameSlice: {trainDataFrameAfterSlice}")
        print(f"testDataFrameSlice: {testDataFrameAfterSlice}")

        return trainDataFrameAfterSlice, testDataFrameAfterSlice

    def applyBatchSize(self, trainDataFrameAfterSlice, testDataFrameAfterSlice, batch_size):
        readyForLearnTrainData = trainDataFrameAfterSlice.batch(batch_size)
        readyForLearnTestData = testDataFrameAfterSlice.batch(batch_size)

        return readyForLearnTrainData, readyForLearnTestData

    def learn(self, readyForLearnTrainData):
        model = tfdf.keras.RandomForestModel(num_trees=100, max_depth=12, min_examples=6)
        model.fit(readyForLearnTrainData)
        print(f"model trained!")
        return model
