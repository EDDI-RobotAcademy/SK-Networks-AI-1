import os

from random_forest.controller.response_form.random_forest_response_form import RandomForestResponseForm
from random_forest.repository.random_forest_repository_impl import RandomForestRepositoryImpl
from random_forest.service.random_forest_service import RandomForestService

import pandas as pd


class RandomForestServiceImpl(RandomForestService):
    def __init__(self):
        self.__randomForestRepository = RandomForestRepositoryImpl()

    def readCsv(self):
        currentDirectory = os.getcwd()
        # print(f"currentDirectory: {currentDirectory}")

        filePath = os.path.join(currentDirectory, '..', 'assets', 'customer_booking.csv')
        # print(f"filePath: {filePath}")

        dataFrame = pd.read_csv(filePath, encoding='latin1')
        # print(f"dataFrame: {dataFrame}")
        return dataFrame  # csv 파일 내용물

    # 특징 타겟 변수를 정의
    def featureTargetVariableDefinition(self, dataEncoded):
        print("featureTargetVariableDefinition()")

        # 최종적으로 알고 싶은 것은 예약완료인지의 여부이므로 얘를 예측할 것으로 상ㅁ음
        # 그렇게 때문에 학습시킬 데이터 X 중 booking-complete란 feature는 빼서 데이터를 재구성한다.
        X = dataEncoded.drop('booking_complete', axis=1)
        y = dataEncoded['booking_complete']

        return X, y

    def randomForestAnalysis(self):
        print("randomForestAnalysis()")

        # csv 파일 읽고 데이터 획득
        dataFrame = self.readCsv()
        # 원래는 얘도 데이터가 5만개라 많아서 비동기 처리를 해야하나 우선은 동기처리로 받아온다.
        dataEncoded, labelEncoders = (
            self.__randomForestRepository.flightCategoricalVariableEncoding(dataFrame))

        # Encoding된 data로 feature 뽑기 (Encoding 왜하냐? -> 모델 학습하기 위해 형태를 변형해주는 작업(전처리과정))
        # 내가 알고 싶은 값을 y로 정하고 나머지 값은 x로 정함
        X, y = self.featureTargetVariableDefinition(dataEncoded)
        # print(f"X: {X}")
        # print(f"y: {y}")

        # 학습, 테스트 데이터 분할
        X_train, X_test, y_train, y_test = (
            self.__randomForestRepository.splitTrainTestSet(X, y))

        # random forest classifier로 모델 학습
        randomForestModel = self.__randomForestRepository.train(X_train, y_train)
        y_pred = self.__randomForestRepository.predict(randomForestModel, X_test)
        accuracy, report, confusionMatrix = (
            self.__randomForestRepository.evaluate(y_test, y_pred))

        # 스모트 적용해보기
        X_resampled, y_resampled = self.__randomForestRepository.applySmote(X_train, y_train)
        # 오버 샘플링된 데이터로 다시 학습
        randomForestModelAfterSmote = self.__randomForestRepository.train(X_resampled, y_resampled)
        # smote데이터 예측 값 얻기
        y_pred_after_smote = (
            self.__randomForestRepository.predict(randomForestModelAfterSmote, X_test))
        # smote 결과 확인
        smoteAccuracy, smoteReport, smoteConfusionMatrix = (
            self.__randomForestRepository.evaluate(y_test, y_pred_after_smote))

        # smote 전 / 후 데이터 return >> 근데 너무 데이터 포맷이 복잡하므로 한번 포장해서 반환 by response form
        # 이렇게 안하면
        return RandomForestResponseForm.createForm(
            confusionMatrix, smoteConfusionMatrix,
            y_test, y_pred, y_pred_after_smote, dataFrame
        )