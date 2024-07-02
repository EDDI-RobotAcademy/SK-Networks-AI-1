from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from decision_tree.repository.decision_tree_repository import DecisionTreeRepository

import pandas as pd
import tensorflow as tf

class DecisionTreeRepositoryImpl(DecisionTreeRepository):
    async def loadWineInfo(self):
        return load_wine()

    async def createDataFrame(self, data, featureNames):
        df = pd.DataFrame(data=data, columns=featureNames)
        return df

    async def splitTrainTestSet(self, dataFrame):
        return train_test_split(dataFrame, test_size=0.2, random_state=42)

    async def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        scaler = StandardScaler()
        # 원래라면 fit 이후 transform을 해야함
        # 그러나 fit_transform은 이것을 한번에 하도록 만들어줌
        # (사실 Domain 관점에선 좀 문제가 있으나 제공해주는 라이브러리이므로 그냥 사용)

        # fit은 데이터를 분석하여 내부 파라미터를 학습하게 됨
        # transform은 학습된 내부 파라미터를 사용하여 데이터를 변환함
        # 고로 transform은 fit이 반드시 먼저 선행되어야 함
        trainDataFrame[featureNames] = scaler.fit_transform(trainDataFrame[featureNames])
        testDataFrame[featureNames] = scaler.transform(testDataFrame[featureNames])

        return trainDataFrame, testDataFrame

    async def sliceTensor(self, scaledTrainDataFrame, scaledTestDataFrame):
        trainDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTrainDataFrame.drop("target", axis=1)),
            scaledTrainDataFrame['target'].astype(int))
        )
        print(f"trainDataFrameAfterSlice: {trainDataFrameAfterSlice}")

