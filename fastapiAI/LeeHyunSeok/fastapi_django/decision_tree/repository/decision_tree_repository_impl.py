from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from decision_tree.repository.decision_tree_repository import DecisionTreeRepository

import tensorflow_decision_forests as tfdf
import pandas as pd
import tensorflow as tf

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
        # 원래라면 fit 이후  transform을 해야함
        # 그러나 fit_transform은 이것을 한 번에 하도록 만들어줌
        # (사실 domain 관전에선 좀 문제가 있으나 제공해주는 라이브러리아므로 그냥 사용)

        # fit은 데이터를 분석하여 내부 파라미터를 학습하게 됨
        # transform은 학습된 내부 파라미터를 사용하여 데이터를 변환함
        # 고로 transform은 fit이 반드시 먼서 선행되어야 함
        trainDataFrame[featureNames] = scaler.fit_transform(trainDataFrame[featureNames])
        testDataFrame[featureNames] = scaler.transform(testDataFrame[featureNames])

        return trainDataFrame, testDataFrame


    def sliceTensor(self, scaledTrainDataFrame, scaledTestDataFrame):

        # from_tensor_slice()는 pandas에서 읽은 데이터를
        # TensorFlow 사용 primitives로 구성하기 위해 필요한 라이브러리입니다.
        # 결론적으로 pandas 데이터 -> TensorFlow 데이터로 만들 때 사용한다고 파악하면 됩니다.
        # 즉, 데이터를 pandas로 딥러닝에 돌리 적합하게 변형한 후 TensorFlow로 딥러닝을 돌리는 거임
        trainDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTrainDataFrame.drop("target", axis=1)),
            scaledTrainDataFrame["target"].astype(int))
        )

        testDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTestDataFrame.drop("target", axis=1)),
             scaledTestDataFrame['target'].astype(int))
        )

        return trainDataFrameAfterSlice, testDataFrameAfterSlice

    def applyBatchSize(self, trainDataFrameAfterSlice, testDataFrameAfterSlice, batchSize):
        readyForLearnTrainData = trainDataFrameAfterSlice.batch(batchSize)
        readyForLearnTestData = testDataFrameAfterSlice.batch(batchSize)

        return readyForLearnTrainData, readyForLearnTestData



    def learn(self, readyForLearnTrainData):
        model = tfdf.keras.RandomForestModel(num_trees=100, max_depth=12, min_exampls=6)
        model.fit(readyForLearnTrainData)

        return model

