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

        wineDataFrame['target'] = wineInfo.target
        # print(f"wineDataFrame: {wineDataFrame}")

        trainDataFrame, testDataFrame = self.decisionTreeRepository.splitTrainTestSet(wineDataFrame)
        scaledTrainDataFrame, scaledTestDataFrame = self.decisionTreeRepository.applyStandardScaler(
            trainDataFrame, testDataFrame, wineInfo.feature_names)

        trainDataFrameAfterSlice, testDataFrameAfterSlice = self.decisionTreeRepository.sliceTensor(
            scaledTrainDataFrame,
            scaledTestDataFrame)

        readyForLearnTrainData, readyForLearnTestData = self.decisionTreeRepository.applyBatchSize(
            trainDataFrameAfterSlice, testDataFrameAfterSlice, 32)

        trainedModel = self.decisionTreeRepository.learn(readyForLearnTrainData)
