from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from random_forest.repository.random_forest_repository import RandomForestRepository
from imblearn.over_sampling import SMOTE
class RandomForestRepositoryImpl(RandomForestRepository):


    def evaluate(self):
        print("evaluate()")

    # 범주형 변수 인코딩
    def flightCategoricalVariableEncoding(self, dataFrame):
        print("flightCategoricalVariableEncoding()")

        labelEncoders = {}
        categoricalColumns = ['sales_channel', 'trip_type', 'flight_day',
                              'route', 'booking_origin'] # 분석에 사용할 label (정답, fields)

        for column in categoricalColumns:
            labelEncoders[column] = LabelEncoder()
            dataFrame[column] = labelEncoders[column].fit_transform(dataFrame[column])

        print(f"dataFrame: {dataFrame}")
        print(f"labelEncoders: {labelEncoders}")
        return dataFrame, labelEncoders

    def splitTrainTest(self, X, y):
        print("splitTrainTest()")

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        # n_estimator : 트리를 몇 개 생성할거냐?
        # (트리는 랜덤 포레스트에서 나오는 트리 개념) = 여러(n)가지 방법으로 시도해보겠다
        randomForestModel = RandomForestClassifier(n_estimators=100, random_state=42)
        randomForestModel.fit(X_train, y_train)

        return randomForestModel

    def predict(self, randomForestModel, X_test):
        y_pred = randomForestModel.predict(X_test)

        return y_pred

    def evaluate(self, y_pred, y_test):
        print("evaluate()")

        accuracy = accuracy_score(y_test, y_pred)
        classificationReport = classification_report(y_test, y_pred)
        confusionMatrix = confusion_matrix(y_test, y_pred)

        return accuracy, classificationReport, confusionMatrix

    def applySmote(self, X_train, y_train):
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
        return X_resampled, y_resampled