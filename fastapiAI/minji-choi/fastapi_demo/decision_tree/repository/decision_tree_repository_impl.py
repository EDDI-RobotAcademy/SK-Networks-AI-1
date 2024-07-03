import pandas as pd
import tensorflow as tf
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from decision_tree.repository.decision_tree_repository import DecisionTreeRepository
# import tensorflow_decision_forests as tfdf

class DecisionTreeRepositoryImpl(DecisionTreeRepository):
    def loadWineInfo(self):
        return load_wine()

    def createDataFrame(self, data, featureNames):
        df = pd.DataFrame(data=data, columns=featureNames)
        return df
    def splitTrainTestSet(self, dataframe):
        return train_test_split(dataframe, test_size=0.2, random_state=42) # defalt. shuffle=True

    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        scaler = StandardScaler()
        trainDataFrame[featureNames] = scaler.fit_transform(trainDataFrame[featureNames])
        testDataFrame[featureNames] = scaler.transform(testDataFrame[featureNames])

        return trainDataFrame, testDataFrame

    def sliceTensor(self, trainDataFrame, testDataFrame):
        # pd.dataFrame -> tensorflow. 데이터 판다스로 만지고 텐서로 변환
        sliceTrainDataFrame = tf.data.Dataset.from_tensor_slices(
            (dict(trainDataFrame.drop("target", axis=1)),trainDataFrame['target'].astype(int))
        )

        sliceTestDataFrame = tf.data.Dataset.from_tensor_slices(
            (dict(testDataFrame.drop("target", axis=1)),testDataFrame['target'].astype(int))
        )

        return sliceTrainDataFrame, sliceTestDataFrame

    def applyBatchSize(self, trainTensor, testTensor, batchSize):
        trainTensor = trainTensor.batch(batchSize)
        testTensor = testTensor.batch(batchSize)
        return trainTensor, testTensor

    def learn(self, trainTensor):
        # model = tfdf.keras.RandomForestModel(num_trees=100, max_depth=12, min_examples=6)
        # model.fit(trainTensor)
        # return model
        print('learning...')



