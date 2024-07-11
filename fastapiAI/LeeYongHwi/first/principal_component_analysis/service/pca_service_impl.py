from principal_component_analysis.repository.pca_repository_impl import PrincipalComponentAnalysisRepositoryImpl
from principal_component_analysis.service.pca_service import PrincipalComponentAnalysisService


class PrincipalComponentAnalysisServiceImpl(PrincipalComponentAnalysisService):

    def __init__(self):
        self.principalComponentAnalysisRepository = PrincipalComponentAnalysisRepositoryImpl()

    def pcaAnalysis(self):
        print("service -> pcaAnalysis")

        numberOfPoints, numberOfFeatures, numberOfComponents = (
            self.principalComponentAnalysisRepository.createPCASample())

        mean = self.principalComponentAnalysisRepository.configZeroMean(numberOfFeatures)
        covariance = self.principalComponentAnalysisRepository.configCovariance(numberOfFeatures)

        createdMultiVariateData = (
            self.principalComponentAnalysisRepository.createMultiVariateNormalDistribution(
                mean, covariance, numberOfPoints)
            )

        print(f"createMultiVariateData {createdMultiVariateData}")

        createdDataFrame = self.principalComponentAnalysisRepository.createDataFrame(
            createdMultiVariateData, numberOfFeatures)

        pca = self.principalComponentAnalysisRepository.readyForAnalysis(numberOfComponents)
        principalComponentList = self.principalComponentAnalysisRepository.fitTransForm(pca, createdDataFrame)

        originalData = createdDataFrame.values.tolist()
        pcaData = principalComponentList.tolist()
        explainVarianceRatio = pca.explained_variance_ratio_.tolist()

        return originalData, pcaData, explainVarianceRatio


