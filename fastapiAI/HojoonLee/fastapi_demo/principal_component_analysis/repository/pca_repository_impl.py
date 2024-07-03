from sklearn.decomposition import PCA

from principal_component_analysis.repository.pca_repository import PrincipalComponentAnalysisRepository
import numpy as np
import pandas as pd
class PrincipalComponentAnalysisRepositoryImpl(PrincipalComponentAnalysisRepository):

    def createPCASample(self):
        numberOfPoints = 333 # 몇개의 점으로 표현할 건지
        numbefOfFeatures = 5 # 뽑을 특징 개수
        numberOfComponents = 2 # 축 개수 >> 2차원

        return numberOfPoints, numbefOfFeatures, numberOfComponents

    def configCovariance(self, numberOfFeatures):
        np.random.seed(42)

        # z-score를 만들기 위해 평균, 분산을 구함 N~(0,1) 따르도록..
        # 왜 공분산을 구하는가 ?
        # 공분산은 실제 상관 관계를 분석할 수 있는 아주 좋은 척도임
        # 우리가 모델을 평가할 때 혼동 행렬을 분석했 듯이
        # 각 종속 변수 간의 상호 연관성을 파악할 때는 이 공분산 행렬을 보면 됨
        # 공분산식은 Covariance(X,y) = 1 / (n-1) SUM [(X샘플 - X평균) * (y샘플 - y평균)] 의 구성을 가짐
        # 만약 X샘플 - X펑균이 이미 정규화 되었다면, 아래 방식과 같이 데이터 행렬과 데이터 전치 행렬의 내적을 하면됨
        # 결과적으로 공분산 행렬은 m x m 형태의 정방 행렬이 됨

        # 그러나 아래쪽에서 갑자기 공분산 파트의 해석이 어려운데,
        # rand()함수 자체가 0~1 사이의 균등분포로 무작위 값을 생성합니다.
        # numberOfFeatures = 5 이므로 5x5 정방행렬이 생성됨
        # 위의 정규화에 따르고 있으므로, 공분산 행렬 계산시 행렬 * 전치행렬이 가능해짐
        # mean = np.zeros(numberOfFeatures)
        covariance = np.random.rand(numberOfFeatures, numberOfFeatures)
        print(f"before dot product covariance : {covariance}")
        covariance = np.dot(covariance, covariance.transpose()) # 행렬과 전치행렬 내적
        print(f"after dot product covariance : {covariance}")

        return covariance

    # 아래 코드에서 mean 파트는 특징 모두의 평균을 0으로 만듭니다.
    # 다중 확률분포를 구성 할 때는 여러 확률 변수들에 대한 평균이 필요합니다.
    def configZeroMean(self, numberOfFeatures):
        mean = np.zeros(numberOfFeatures)
        return mean

    def createMultiVariateNormalDistribution(self, mean, covariance, numberOfPoints):
        # np가 다중 확률 분포 만드는 것을 서포트함
        return np.random.multivariate_normal(mean, covariance, numberOfPoints)

    def createDataFrame(self, createdMultiVariateData, numberOfFeatures):
        # field명 : feature_1 ~ feature_5
        return pd.DataFrame(data=createdMultiVariateData,
                            columns=[f'feature_{i}' for i in range(1, numberOfFeatures + 1)])

    # 주성분 분석을 위한 Scikit Learn 라이브러리의 제공함수입니다.
    # 예로 원래 데이터가 10개의 변수를 가지고 있다면
    # 지정한 n_components의 개수로 주성분 분석을 위한 준비를 해줍니다. (차원축소)
    def readyForAnalysis(self, numberOfComponents):
        # numberOfComponents = 2
        return PCA(n_components=numberOfComponents)

    def fitTransform(self, pca, createdDataFrame):
        # 학습 후 normalize 까지
        # pca를 통해 차원을 축소시키고 축소시킨 영역에 대해서도 데이터가 흩어져 있을 수 있으므로 >> normalize 진행
        return pca.fit_transform(createdDataFrame)
