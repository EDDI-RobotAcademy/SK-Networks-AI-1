from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from random_forest.repository.random_forest_repository import RandomForestRepository
from imblearn.over_sampling import SMOTE


class RandomForestRepositoryImpl(RandomForestRepository):

    def evaluate(self, y_test, y_pred):
        print("evaluate()")

        accuracy = accuracy_score(y_test, y_pred)
        classificationReport = classification_report(y_test, y_pred)
        confusionMatrix = confusion_matrix(y_test, y_pred)

        return accuracy, classificationReport, confusionMatrix

    # 범주형 변수 인코딩
    def flightCategoricalVariableEncoding(self, dataFrame):
        print("flightCategoricalVariableEncoding()")

        labelEncoders = {}
        categoricalColumns = [
            'sales_channel', 'trip_type', 'flight_day', 'route', 'booking_origin'
        ]

        for column in categoricalColumns:
            labelEncoders[column] = LabelEncoder()
            dataFrame[column] = labelEncoders[column].fit_transform(dataFrame[column])

        # print(f"dataFrame: {dataFrame}")
        # print(f"labelEncoders: {labelEncoders}")
        return dataFrame, labelEncoders

    def splitTrainTestSet(self, X, y):
        print("splitTrainTestSet()")

        X_train, X_test, y_train, y_test = (
            train_test_split(X, y, test_size=0.2, random_state=42))

        # print(f"X_train: {X_train}")
        # print(f"X_test: {X_test}")
        # print(f"y_train: {y_train}")
        # print(f"y_test: {y_test}")

        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        # 트리를 100개 생성
        # 랜덤 포레스트의 경우 여러 개의 결정 트리를 구성하게 됩니다.
        # 좀 더 정확하게 100개의 결정 트리를 만들어 보겠다는 의미로 보면 되겠습니다.
        # 각각의 개별 트리는 데이터를 분할하여 예측을 수행할 수 있습니다.
        # 고로 총 100개의 예측들이 있다는 소리입니다.
        
        # 모든 트리는 (100개)는 독립적으로 예측을 진행 (위의 얘기와 동일선상)
        # 최종적으로 100개의 트리에서 나온 결과를 종합하여 결론을 내리게 됨
        # 각각의 트리들에서 확보한 평균값을 가지고 예측을 만듬

        # 데이터가 많은 상황에서 이상한 학습이 진행되는 overfitting(과적합)이 방지된다는 이점이 큼
        # 결정 트리의 숫자가 많을수록 전반적인 성능이 좋아지지만
        # 일정 숫자 이상이 되면 성능 개선이 미미하며
        # 응답 속도가 떨어지기 때문에 여러모로 트레이드 오프가 중요함
        randomForestModel = RandomForestClassifier(n_estimators=100, random_state=42)
        randomForestModel.fit(X_train, y_train)

        return randomForestModel

    def predict(self, randomForestModel, X_test):
        y_pred = randomForestModel.predict(X_test)

        return y_pred

    # SMOTE (Synthetic Minority Over-sampling TEchnique)
    # 불균형 데이터셋에서 소수 클래스의 데이터를 증강하여 데이터 균형을 맞춤
    # 분류 문제에서 소수의 집합은 데이터가 부족함
    # 이런 소수 집합의 성능을 높이고자 할 때 사용하면 효율적
    def applySmote(self, X_train, y_train):
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

        return X_resampled, y_resampled


