from sklearn.preprocessing import LabelEncoder

from random_forest.repository.random_forest_repository import RandomForestRepository


class RandomForestRepositoryImpl(RandomForestRepository):
    def evaluate(self):
        print("evaluate()")

    def flightCategoricalVariableEncoding(self, dataFrame):
        print("flightCategoricalVariableEncoding()")

        labelEncoders = {}
        categoricalColumns = [
            'sales_channel', 'trip_type', 'flight_day', 'route', 'booking_origin'
        ]

        for column in categoricalColumns:
            labelEncoders[column] = LabelEncoder()
            dataFrame[column] = labelEncoders[column].fit_transform(dataFrame[column])

        print(f"dataFrame: {dataFrame}")
        print(f"labelEncoders: {labelEncoders}")
        return dataFrame, labelEncoders
