from decision_tree.repository.decision_tree_repository_impl import DecisionTreeRepositoryImpl
from decision_tree.service.decision_tree_service import DecisionTreeService


class DecisionTreeServiceImpl(DecisionTreeService):

    def __init__(self):
        self.decisionTreeRepository = DecisionTreeRepositoryImpl()
    async def decisionTreeTrain(self):
        print("service -> decisionTreeTrain()")

        wineInfo = await self.decisionTreeRepository.loadWineInfo()
        # print(f"wine feature names: {wineInfo.feature_names}")

        wineDataFrame = await self.decisionTreeRepository.createDataFrame(wineInfo.data, wineInfo.feature_names)
        wineDataFrame['target'] = wineInfo.target
        # print(f"wine data frame: {wineDataFrame}")

        trainDataFrame, testDataFrame = await self.decisionTreeRepository.splitTrainTestSet(wineDataFrame)

        scaledTrainDataFrame, scaledTestDataFrame =\
            await self.decisionTreeRepository.applyStandardScaler(trainDataFrame, testDataFrame, wineInfo.feature_names)
        # print(f"scaledTrainDataFrame: {scaledTrainDataFrame}")
        # print(f"scaledTestDataFrame: {scaledTestDataFrame}")

        await self.decisionTreeRepository.sliceTensor(scaledTrainDataFrame, scaledTestDataFrame)