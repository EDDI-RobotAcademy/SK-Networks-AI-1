from principal_component_analysis.repository.pca_repository_impl import PrincipalComponentAnalysisRepositoryImpl
from principal_component_analysis.service.pca_service import PrincipalComponentAnalysisService


class PrincipalComponentAnalysisServiceImpl(PrincipalComponentAnalysisService):

    def __init__(self):
        self.principalComponentAnalysisRepository = PrincipalComponentAnalysisRepositoryImpl()

    def pcaAnalysis(self):
        print(f"service -> pcaAnalysis()")

        numberOfPoints, numberOfFeatures, numberOfComponents = (
            self.principalComponentAnalysisRepository.createPCASample())
        print(numberOfPoints)
        print(numberOfFeatures)
        print(numberOfComponents)

        mean = self.principalComponentAnalysisRepository.configZeroMean(numberOfFeatures)
        covariance = self.principalComponentAnalysisRepository.configCovariance(numberOfFeatures)

        createMultiVariateData = (
            self.principalComponentAnalysisRepository.createMultiVariateNormalDistribution(mean, covariance,
                                                                                           numberOfPoints))

        print(f"createdMultiVariateData: {createMultiVariateData}")

        createdDataFrame = self.principalComponentAnalysisRepository.createDataFrame(createMultiVariateData,
                                                                                     numberOfFeatures)

        print(f"createdDataFrame: \n{createdDataFrame}")

        pca = self.principalComponentAnalysisRepository.readyForAnalysis(numberOfComponents)
        principalComponentList = self.principalComponentAnalysisRepository.fitTransform(pca, createdDataFrame)

        originalData = createdDataFrame.values.tolist()
        pcaData = principalComponentList.tolist()
        explainedVarianceRatio = pca.explained_variance_ratio_.tolist()

        return originalData, pcaData, explainedVarianceRatio
