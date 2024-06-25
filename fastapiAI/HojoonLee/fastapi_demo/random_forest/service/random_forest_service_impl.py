import os
import pandas as pd

from random_forest.controller.random_forest_response_form import RandomForestResponseForm
from random_forest.repository.random_forest_repository_impl import RandomForestRepositoryImpl
from random_forest.service.random_forest_service import RandomForestService

class RandomForestServiceImpl(RandomForestService):

    def __init__(self):
        self.__randomForestRepository = RandomForestRepositoryImpl()

    def readCsv(self):
        currentDirectory = os.getcwd() # 현재 경로 가져오기
        #print(f"currentDireoctory: {currentDirectory}") # ~~/fastapi_demo/app 으로 뜸

        # app에는 data없으므로 데이터가 잇는 경로로 다시 맞춰주기
        filePath = os.path.join(currentDirectory, '..', 'assets', 'customer_booking.csv')
        #print(f"filePath: {filePath}") : fastapi_demo/assets//customer_booking.csv

        dataFrame = pd.read_csv(filePath, encoding='latin1')
        #print(f"dataFrame: {dataFrame}")
        return dataFrame # csv 파일 내용물

    def featureTargetVariableDefinition(self, dataEncoded):
        print(f"featureTargetVariableDefinition()")

        # 최종적으로 알고싶은 것은 예약완료인지의 여부이므로 얘를 예측할 것으로 삼음
        # 그렇기 때문에 학습시킬 데이터 X 중 booking_complete란 feature는 빼서 데이터를 재구성한다.
        X = dataEncoded.drop('booking_complete', axis=1)
        y = dataEncoded['booking_complete']

        return X, y

    def randomForestAnalysis(self):
        print("randomForestAnalysis()")

        # csv 파일 읽고 데이터 획득하기
        dataFrame = self.readCsv()
        # 원래는 얘도 데이터가 5만개라 많아서 비동기 처리를 해야하나 우선은 동기처리로 받아온다.
        dataEncoded, labelEncoders = self.__randomForestRepository.flightCategoricalVariableEncoding(dataFrame)

        # Encoding된 data로 feature 뽑기 (Encoding 왜하냐? -> 모델 학습하기위해 형태를 변형해주는 작업)
        X, y = self.featureTargetVariableDefinition(dataEncoded)
        # print(f"X: {X}")
        # print(f"y: {y}")

        # 학습, 테스트 데이터 분할
        # 원래는 여기 과정도 비동기로 진행이 되어야 함 (데이터가 많아서)
        X_train, X_test, y_train, y_test = self.__randomForestRepository.splitTrainTest(X,y)

        # random forest classifier로 모델 학습
        # random forest는 다양한 경우의 수로 평균을 내기에 과적합은 확실히 방지됨
        # 하지만 경우의 수가 많아질 수록 퍼포먼스 상향은 미미한데, 시간이 오래걸림 (그러므로 trade-off를 잘 설정하자)
        randomForestModel = self.__randomForestRepository.train(X_train, y_train)
        # 학습된 모델로 test 하기
        y_pred = self.__randomForestRepository.predict(randomForestModel, X_test)
        # 예측값과 실제 정답사이 정확도 비교
        accuracy, report, confusionMatrix = self.__randomForestRepository.evaluate(y_pred, y_test)

        # 스모트 적용해보기
        X_resampled, y_resampled = self.__randomForestRepository.applySmote(X_train,y_train)
        # 오버 샘플링된 데이터로 다시 학습
        randomForestModelAfterSmote = self.__randomForestRepository.train(X_resampled, y_resampled)
        # smote데이터 예측 값 얻기
        y_pred_after_smote = self.__randomForestRepository.predict(randomForestModelAfterSmote, X_test)
        # smote 결과 확인
        smoteAccuracy, smoteReport, smoteConfusionMatrix = (
            self.__randomForestRepository.evaluate(y_pred_after_smote, y_test))

        # smote 전/후 데이터 return >> 근데 너무 데이터 포맷이 복잡하므로 한번 포장해서 반환한다. by ResponseForm
        # 이렇게 안 하면 데이터 형태에 따라 포장 방법이 달라져서 해당 코드가 길어져서 가독성 떨어짐
        return RandomForestResponseForm.createForm(
            confusionMatrix, smoteConfusionMatrix,
            y_test, y_pred, y_pred_after_smote, dataFrame
        )
