from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from orders_analysis.repository.orders_analysis_repository import OrdersAnalysisRepository


class OrdersAnalysisRepositoryImpl(OrdersAnalysisRepository):

    async def prepareViewCountVsQuantity(self, dataFrame):
        X = dataFrame['viewCount'].values.reshape(-1, 1)
        y = dataFrame['quantity'].values

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        return X_scaled, y, scaler

    async def splitTrainTestData(self, X_scaled, y):
        X_train, y_train, X_test, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        return X_train, y_train, X_test, y_test


