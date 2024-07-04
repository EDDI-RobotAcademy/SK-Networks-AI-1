from decision_tree.repository.decision_tree_repository_impl import DecisionTreeRepositoryImpl
from decision_tree.service.decision_tree_service import DecisionTreeService


class DecisionTreeServiceImpl(DecisionTreeService):

    def __init__(self):
        self.decisionTreeRepository = DecisionTreeRepositoryImpl()

    def decisionTreeTrain(self):
        print("service -> decisionTreeTrain()")

        wineInfo = self.decisionTreeRepository.loadWineInfo()
        # print(f"wine feature names: {wineInfo.feature_names}")

        wineDataFrame = self.decisionTreeRepository.createDataFrame(wineInfo.data, wineInfo.feature_names)

        # 타겟 세팅
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

        # 모델한테 32개의 샘플들을 주고 학습시키는 것 -> batch size 가 끝나면 딥러닝만 시키면 됨
        # tensor화 시켰으므로 학습시키기 전 batchsize 조정
        # 학습의 효율을 위해서 사용 (GPU의 병렬처리 장점을 이용해서 자원 관리 효율적으로)
        readyForLearnTrainData, readyForLearnTestData = self.decisionTreeRepository.applyBatchSize(
            trainDataFrameAfterSlice,
            testDataFrameAfterSlice,
            32
        )

        trainedModel = self.decisionTreeRepository.learn(readyForLearnTrainData)



