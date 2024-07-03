from imblearn.over_sampling import SMOTE
from random_forest.repository.random_forest_repository import RandomForestRepository
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class RandomForestRepositoryImpl(RandomForestRepository):
    def evaluate(self, y_test, y_pred):
        print('evaluate()')
        accuracy = accuracy_score(y_test, y_pred)
        classificationReport = classification_report(y_test, y_pred)
        confusionMatrix = confusion_matrix(y_test, y_pred)
        return accuracy, classificationReport, confusionMatrix

    def flightCategoricalVariableEncoding(self, dataFrame):
        # print('flightCategoricalVariableEncoding()')
        labelEncoders = {}
        categoricalColumns = ['sales_channel','trip_type','flight_day','route','booking_origin']

        for column in categoricalColumns:
            labelEncoders[column] = LabelEncoder()
            dataFrame[column] = labelEncoders[column].fit_transform(dataFrame[column])
        # print(f'dataFrame : {dataFrame}')
        # print(f'labelEncoders : {labelEncoders}')

        return dataFrame, labelEncoders


    def splitTrainTestSet(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

        # print(f"X_train : {X_train}")
        # print(f"X_test : {X_test}")
        # print(f"y_train : {y_train}")
        # print(f"y_test : {y_test}")
        return X_train, X_test, y_train, y_test

    def train(self, X_train, y_train):
        randomForestmodel = RandomForestClassifier(n_estimators=100, random_state=42)  # 트리 100개 생성
        randomForestmodel.fit(X_train, y_train)
        return randomForestmodel

    def predict(self, randomForestModel, X_test):
        y_pred = randomForestModel.predict(X_test)
        return y_pred
    def applysmote(self, X_train, y_train):
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
        return X_resampled, y_resampled
