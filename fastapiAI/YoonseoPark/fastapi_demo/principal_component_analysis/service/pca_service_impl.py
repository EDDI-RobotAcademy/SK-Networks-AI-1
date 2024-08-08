from principal_component_analysis.repository.pca_repository_impl import PrincipalComponentAnalysisRepositoryImpl
from principal_component_analysis.service.pca_service import PrincipalComponentAnalysisService


class PrincipalComponentAnalysisServiceImpl(PrincipalComponentAnalysisService):

    def __init__(self):
        self.principalComponentAnalysisRepository = PrincipalComponentAnalysisRepositoryImpl()

    async def pcaAnalysis(self):
        print("service -> pcaAnalysis()")

        numberOfPoints, numberOfFeatures, numberOfComponents\
            = await self.principalComponentAnalysisRepository.createPCASample()

        mean = await self.principalComponentAnalysisRepository.configZeroMean(numberOfFeatures)
        covariance = await self.principalComponentAnalysisRepository.configCovariance(numberOfFeatures)

        createdMultiVariateData =\
            await self.principalComponentAnalysisRepository.createMultiVariateNormalDistribution(mean, covariance, numberOfPoints)
        # print(f"createdMultiVariateData: {createdMultiVariateData}")

        createdDataFrame =\
            await self.principalComponentAnalysisRepository.createDataFrame(createdMultiVariateData, numberOfFeatures)

        pca = await self.principalComponentAnalysisRepository.readyForAnalysis(numberOfComponents)
        principalComponentList = await self.principalComponentAnalysisRepository.fitTransform(pca, createdDataFrame)

        originalData = createdDataFrame.values.tolist()
        pcaData = principalComponentList.tolist()
        explainedVarianceRatio = pca.explained_variance_ratio_.tolist()

        return originalData, pcaData, explainedVarianceRatio