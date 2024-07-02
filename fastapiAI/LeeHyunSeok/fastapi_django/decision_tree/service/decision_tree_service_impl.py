from joblib import dump

from decision_tree.repository.decision_tree_repository_impl import DecisionTreeRepositoryImpl
from decision_tree.service.decision_tree_service import DecisionTreeService


class DecisionTreeServiceImpl(DecisionTreeService):
    FEATURE_NAMES_PATH = 'wine_feature_name.joblib'
    TARGET_NAMES_PATH = 'wine_target_name.joblib'
    TRAINED_MODEL_PATH = 'wine_trained_model.h5'

    def __init__(self):
        self.decisionTreeRepository = DecisionTreeRepositoryImpl()

    def decisionTreeTrain(self):
        print("service -> decisionTreeTrain()")

        # 와인 정보 담기
        wineInfo = self.decisionTreeRepository.loadWineInfo()
        # print(f"wine feature names: {wineInfo.feature_names}")

        # dataFrame 만들기 == csv화
        wineDataFrame = self.decisionTreeRepository.createDataFrame(
                                    wineInfo.data, wineInfo.feature_names)

        # csv로부터 알고 싶은 target정보 지정 ==> y
        # wineDataFrame에 target이라는 field 추가
        # 해당 정보에는 load_wine에 내장된 기능인 target으로 와인 label(정답)이 담김
        wineDataFrame['target'] = wineInfo.target
        # print(f"wineDataFrame: {wineDataFrame}")


        # 데이터 분할
        trainDataFrame, testDataFrame = self.decisionTreeRepository.splitTrainTestSet(wineDataFrame)
        scaledTrainDataFrame, scaledTestDataFrame = self.decisionTreeRepository.applyStandardScaler(
                                trainDataFrame, testDataFrame, wineInfo.feature_names)

        trainDataFrameAfterSlice, testDataFrameAfterSlice = self.decisionTreeRepository.sliceTensor(
            scaledTrainDataFrame,
            scaledTestDataFrame
        )


        # tensor화 시켰으므로 학습시키기 전 batchsize 조정
        # batch: 1번의 학습에 데이터(샘플)를 몇개씩 줄 것인가?
        # 학습의 효율을 위해서 사용한다. (gpu의 병렬처리 장점을 활용하기 위해서 사용)
        readyForLearnTrainData, readyForLearnTestData = self.decisionTreeRepository.applyBatchSize(
            trainDataFrameAfterSlice,
            testDataFrameAfterSlice,
            32
        )

        trainedModel = self.decisionTreeRepository.learn(readyForLearnTrainData)

        dump(wineInfo.feature_names, self.FEATURE_NAMES_PATH)
        dump(wineInfo.target_names, self.TARGET_NAMES_PATH)
        dump(trainedModel, self.TRAINED_MODEL_PATH)