import os

from fastapi import APIRouter, Depends, HTTPException, status
from joblib import load

from principal_component_analysis.service.pca_service_impl import PrincipalComponentAnalysisServiceImpl

async def injectPrincipalComponentAnalysisService() -> PrincipalComponentAnalysisServiceImpl:
    return PrincipalComponentAnalysisServiceImpl()

PrincipalComponentAnalysisRouter = APIRouter()

@PrincipalComponentAnalysisRouter.get("/pca-train")
async def pcaAnalysis(principalComponentAnalysisService: PrincipalComponentAnalysisServiceImpl =
                        Depends(injectPrincipalComponentAnalysisService)):

    print(f"controller -> pcaAnalysis()")
    originalData, pcaData, explainedVarianceRatio = principalComponentAnalysisService.pcaAnalysis()

    return {
        "original_data":originalData,
        "pca_data":pcaData,
        "explained_variance_ratio":explainedVarianceRatio
    }
