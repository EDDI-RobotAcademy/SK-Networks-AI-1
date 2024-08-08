from joblib import dump
from decision_tree.service.decision_tree_service import DecisionTreeService
from decision_tree.repository.decision_tree_repository_impl import DecisionTreeRepositoryImpl
class DecisionTreeServiceImpl(DecisionTreeService):
    FEATURE_NAMES_PATH = 'wine_feature_name.joblib'
    TARGET_NAMES_PATH = 'wine_target_name.joblib'
    TRAINED_MODEL_PATH = 'wine_trained_model.h5'

    def __init__(self):
        self.decisionTreeRepository = DecisionTreeRepositoryImpl()

    def decisionTreeTrain(self):
        print("service -> decisionTreeTrain()")

        # 와인을 구성한 성분들이 담김
        wineInfo = self.decisionTreeRepository.loadWineInfo()
        print(f"wine feature names: {wineInfo.feature_names}")

        # dataframe 만들기 == csv화
        wineDataFrame = self.decisionTreeRepository.createDataFrame(wineInfo.data, wineInfo.feature_names)
        print(f"wineDataFrame: {wineDataFrame}") # 13개의 featuer, 177개의 데이터

        # csv로 부터 알고 싶은 target 정보 지정 ==> y
        # wineDataFrame에 target이란 field 추가
        # 해당 정보에는 load_wine에 내장된 기능인 target으로 와인 label(정답)이 담김
        wineDataFrame['target'] = wineInfo.target
        print(f"add target fields wineDataFrame: {wineDataFrame}")

        # data 분할
        trainDataFrame, testDataFrame = self.decisionTreeRepository.splitTrainTestSet(wineDataFrame)

        # scaler 적용 ==> normalize를 위함
        # wineInfo.feature_names 를 함께 보내서 featuring 용도로 활용
        scaledTrainDataFrame, scaledTestDataFrame= (self.decisionTreeRepository.applyStandardScaler
                                                    (trainDataFrame, testDataFrame, wineInfo.feature_names))

        # pd -> tensor
        trainedDataFrameAfterSlice, testedDataFrameAfterSlice = self.decisionTreeRepository.sliceTensor(
            scaledTrainDataFrame, scaledTestDataFrame)

        # tensor화 시켰으므로 학습시키기 전 batchsize 조정
        # batch : 1번의 학습에 한번에 몇개씩 데이터(샘플)를 줄것인가?
        readyForLearnTrainData, readyForLearnTestData = self.decisionTreeRepository.applyBatchSize(
            trainedDataFrameAfterSlice,
            testedDataFrameAfterSlice,
            32
        )

        # 학습
        trainedModel = self.decisionTreeRepository.learn(readyForLearnTrainData)
        # 학습 모델 저장
        dump(wineInfo.feature_names, self.FEATURE_NAMES_PATH)
        dump(wineInfo.target_names, self.TARGET_NAMES_PATH)
        dump(trainedModel, self.TRAINED_MODEL_PATH)