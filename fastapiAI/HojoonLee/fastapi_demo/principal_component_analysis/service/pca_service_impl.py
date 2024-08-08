from principal_component_analysis.repository.pca_repository_impl import PrincipalComponentAnalysisRepositoryImpl
from principal_component_analysis.service.pca_service import PrincipalComponentAnalysisService

class PrincipalComponentAnalysisServiceImpl(PrincipalComponentAnalysisService):

    def __init__(self):
        self.principalComponentAnalysisRepository = PrincipalComponentAnalysisRepositoryImpl()

    def pcaAnalysis(self):
        print(f"service -> pcaAnalysis()")

        # pca 분석을 위해 필요한 요소들 3개 세팅
        numberOfPoints, numberOfFeatures, numberOfComponents = self.principalComponentAnalysisRepository.createPCASample()

        # 평균과 공분산 구하기 >> z-score 구하기 위함
        mean = self.principalComponentAnalysisRepository.configZeroMean(numberOfFeatures)
        covariance = self.principalComponentAnalysisRepository.configCovariance(numberOfFeatures)

        # 평균, 공분산을 입력으로 다중확률분포 구성
        # createdMultiVariateData는 (333,5)의 행렬인 상태 >> 333개의 점마다 랜덤값을 부여?
        createdMultiVariateData = (self.principalComponentAnalysisRepository.
                                   createMultiVariateNormalDistribution(mean, covariance, numberOfPoints))
        print(f"createdMultiVariateData : {createdMultiVariateData.shape}")

        # dataframe 구성
        createdDataFrame = self.principalComponentAnalysisRepository.createDataFrame(
            createdMultiVariateData, numberOfFeatures)

        # pca 초기 설정 : 차원 축소 진행
        pca = self.principalComponentAnalysisRepository.readyForAnalysis(numberOfComponents)

        #주성분 분석(pca) 시작
        principalComponentList = self.principalComponentAnalysisRepository.fitTransform(pca, createdDataFrame)

        originalData = createdDataFrame.values.tolist() # pca 이전의 데이터들을 list에 담음
        pcaData = principalComponentList.tolist() # pca 적용 이후 데이터들을 list에 담음
        explainedVarianceRatio = pca.explained_variance_ratio_.tolist() # 공분산값 저장

        return originalData, pcaData, explainedVarianceRatio