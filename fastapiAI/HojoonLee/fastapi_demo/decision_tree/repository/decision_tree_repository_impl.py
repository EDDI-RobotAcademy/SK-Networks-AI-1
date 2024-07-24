from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from decision_tree.repository.decision_tree_repository import DecisionTreeRepository
import pandas as pd
import tensorflow as tf

# pip install tensorflow_decision_forests
# 위에 해도 만약 에러난다면 pip install --upgrade typing_extensions 까지 해준다.
import tensorflow_decision_forests as tfdf

class DecisionTreeRepositoryImpl(DecisionTreeRepository):

    def loadWineInfo(self):
        return load_wine()

    def createDataFrame(self, data, featureNames):
        # dataframe으로 쓸 data는 입력받은 wineData, 각 field는 featureNames로 설정
        df = pd.DataFrame(data=data, columns=featureNames)
        return df

    def splitTrainTestSet(self, dataFrame):
        return train_test_split(dataFrame, test_size=0.2, random_state=42)

    def applyStandardScaler(self, trainDataFrame, testDataFrame, featureNames):
        scaler = StandardScaler()
        # 원래라면 fit 이후 transform을 해야함
        # 그러나 fit_transform은 위 과정을 한 번에 하도록 만들어줌
        # 근데 현재(240702) python 3.10 ver까지만 지원하는 듯? >> python 3.12는 지원을 안 함
        # (사실 Domain 관점에선 문제가 있으나 제공해주는 라이브러리이므로 그냥 사용)

        # fit은 데이터를 분석하여 내부 파라미터를 학습하게 됨
        # transform은 학습된 내부 파라미터를 사용하여 데이터를 변환함 (normalize 역할)
        # 고로 trnasform은 fit이 반드시 선행되어야 함
        trainDataFrame[featureNames] = scaler.fit_transform(trainDataFrame[featureNames])
        testDataFrame[featureNames] = scaler.transform((testDataFrame[featureNames]))

        return trainDataFrame, testDataFrame

    def sliceTensor(self, scaledTrainDataFrame, scaledTestDataFrame):
        # csv -> tensor화
        # from_tensor_slices()는 pandas에서 읽은 데이터를
        # TensorFlow 사용 primitives로 구성하기 위해 필요한 라이브러리입니다.
        # 결론적으로 pandas 데이터 -> TensorFlow 데이터로 만들 때 사용한다고 파악하면 됩니다.
        # 입력 데이터는 y인 target빼고 만듦
        trainedDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTrainDataFrame.drop("target", axis=1)),
            scaledTrainDataFrame['target'].astype(int))
        )

        testedDataFrameAfterSlice = tf.data.Dataset.from_tensor_slices(
            (dict(scaledTestDataFrame.drop("target", axis=1)),
             scaledTestDataFrame['target'].astype(int))
        )

        # print(f"trainedDataFrameAfterSlice : {trainedDataFrameAfterSlice}")
        return trainedDataFrameAfterSlice, testedDataFrameAfterSlice

    def applyBatchSize(self, trainedDataFrameAfterSlice, testedDataFrameAfterSlice, batchSize):
        # tf.Tensor화 시켰기 때문에 .batch의 기능을 이용 가능 (내장 기능)
        readyForLearnTrainData = trainedDataFrameAfterSlice.batch(batchSize)
        readyForLearnTestData = testedDataFrameAfterSlice.batch(batchSize)

        return readyForLearnTrainData, readyForLearnTestData

    def learn(self, readyForLearnTrainData):
        # tf도 randomForest를 지원함 (조금 세팅을 다르게 하지만) by tfdf
        # 초기 모델을 randomForest 모델로 설정
        model = tfdf.keras.RandomForestModel(num_trees=100, max_depth=12, min_examples=6)
        # 모델 학습
        model.fit(readyForLearnTrainData)
        return model