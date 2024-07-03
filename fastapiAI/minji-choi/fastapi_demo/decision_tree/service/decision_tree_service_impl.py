import numpy as np
import os
from decision_tree.repository.decision_tree_repository_impl import DecisionTreeRepositoryImpl
from decision_tree.service.decision_tree_service import DecisionTreeService

class DecisionTreeServiceImpl(DecisionTreeService):
    SAVED_MODEL_PATH = 'decision_tree_model.npz'
    def __init__(self):
        self.decisionTreeRepository = DecisionTreeRepositoryImpl()
    def saveTrainedModel(self, trainedModel, path):
        # np.savez(path, weight=trainedModel.weight.numpy(), intercept=trainedModel.intercept.numpy())
        print(f'model saved at {os.path.join(os.getcwd(),path)}')

    def decisionTreeTrain(self):
        print('service -> decisionTreeTrain()')
        # load data
        wineInfo = self.decisionTreeRepository.loadWineInfo()
        wineDataFrame = self.decisionTreeRepository.createDataFrame(wineInfo.data, wineInfo.feature_names)
        wineDataFrame['target'] = wineInfo.target

        # tran test split
        trainDataFrame, testDataFrame = self.decisionTreeRepository.splitTrainTestSet(wineDataFrame)
        print('trainDataFrame : ', trainDataFrame)
        print('testDataFrame : ', testDataFrame)

        # scaling(nomalization)
        trainDataFrame, testDataFrame = self.decisionTreeRepository.applyStandardScaler(trainDataFrame, testDataFrame, wineInfo.feature_names)
        print('trainDataFrame after scaling : ', trainDataFrame)
        print('testDataFrame after scaling : ', testDataFrame)

        # tensor로 변환
        trainTensor, testTensor = self.decisionTreeRepository.sliceTensor(trainDataFrame, testDataFrame)
        print('trainTensor after slicing : ', trainDataFrame)
        print('testTensor after slicing : ', testDataFrame)

        # applying batch size
        trainTensor, testTensor = self.decisionTreeRepository.applyBatchSize(trainTensor, testTensor, 32)
        print('trainTensor applying batch : ', trainTensor)
        print('testTensor applying batch : ', testTensor)

        # Training
        trainModel = self.decisionTreeRepository.learn(trainTensor)

        # trainedModel = await self.decisionTreeRepository.trainModel(selectedModel, X, y)
        #
        #
        # self.saveTrainedModel(trainedModel, self.SAVED_MODEL_PATH)
        # return True