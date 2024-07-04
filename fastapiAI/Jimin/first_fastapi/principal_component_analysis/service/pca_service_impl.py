from principal_component_analysis.repository.pca_repository_impl import \
    PrincipalComponentAnalysisRepositoryImpl
from principal_component_analysis.service.pca_service import PrincipalComponentAnalysisService


class PrincipalComponentAnalysisServiceImpl(PrincipalComponentAnalysisService):

    def __init__(self):
        self.principalComponentAnalysisRepository = PrincipalComponentAnalysisRepositoryImpl()

    def pcaAnalysis(self):
        print("service -> pcaAnalysis()")

        numberOfPoints, numberOfFeatures, numberOfComponents = (
            self.principalComponentAnalysisRepository.createPCASample())

        # 가우시안 분포를 따르려면 평균이 0, 분산이 1이어야 하기 때문에 mean(평균)값을 0으로 잡아준다.
        mean = self.principalComponentAnalysisRepository.configZeroMean(numberOfFeatures)
        covariance = self.principalComponentAnalysisRepository.configCovariance(numberOfFeatures)

        createdMultiVariateData = (
            self.principalComponentAnalysisRepository.createMultiVariateNormalDistribution(mean, covariance, numberOfPoints))

        print(f"createdMultiVariateData: {createdMultiVariateData}")

        createdDataFrame = self.principalComponentAnalysisRepository.createDataFrame(
            createdMultiVariateData, numberOfFeatures)

        pca = self.principalComponentAnalysisRepository.readyForAnalysis(numberOfComponents)
        # 주 성분 뽑아오기
        principalComponentList = self.principalComponentAnalysisRepository.fitTransform(pca, createdDataFrame)

        originalData = createdDataFrame.values.tolist()
        pcaData = principalComponentList.tolist()
        explainedVarianceRatio = pca.explained_variance_ratio_.tolist()

        return originalData, pcaData, explainedVarianceRatio

