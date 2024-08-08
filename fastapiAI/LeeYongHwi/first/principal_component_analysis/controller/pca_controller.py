import os
import tensorflow as tf

import joblib
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from principal_component_analysis.service.pca_service_impl import PrincipalComponentAnalysisServiceImpl

# PCA (Principal Component Analysis)라는 주성분 분석이라는 이름을 가지고 있음
# 제일 중요한 특징이라면 고차원의 데이터를 분석할 때 주요 특징들은 유지하면서
# 데이터를 저차원 공간으로 보낼 수 있다는 것이 매우 훌륭한 기법
# 고차원의 데이터란 것은 결국 데이터를 판정할 때 사요ㅕㅇ하는 파라미터가 여러 개 있다는 뜻
# 쉽게 얘기해서 ax^n + bx^(n-1) - cx^(n-2) + ... + zx^(n-1004) + ... +
# 위와 같은 형태로 표현 되는 케이스를 좀 더 단순화 시켜서 유사한 혹은 동일한 모양을 만들어 내는 것
# 위 케이스는 결국 n차원이지만 PCA를 통해서 이 n차원을 n-x차원으로 줄일 수 있다는 것이 핵심
# 설명을 위해 2차원으로 했지만 3차원, 4차원 등등 관여하는 종속 변수가 더 많을 수 있음
# 실제로 PCA 분석은 분산 (Variance)를 최대화 하는 축(Principal Component)을 찾는 것이 핵심
# Principal Component Analysis라고 이름이 붙은 이유가
# 결국 분산을 최대화하는 주성분을 찾아 분석하는 기법이기 때문
# PCA는 결국 분산값을 최대화하는 새로운 좌표계를 생성
# 이렇게 여러 종속 변수들이 존재하는 영역에서 반드시 다뤄지는 것이 있는데
# 바로 공분산(Co-variance)이라는 녀석
# 실제로 PCA는 공분산 행렬을 사용하여 데이터의 분산과 상관관계를 분석함
# 공분산 행렬의 고유값(eigenvalue)과 고유벡터(eigenvector)를 계산하여 데이터 주성분을 찾음
# 피보나치 수열의 일반화를 위해서도 고유값과 고유벡터를 사용
# 여기서 고유값이 크고 작은 것은 상당히 중요한 척도가 됨
# 고유값이 크면 클 수록 해당 벡터 방향으로의 분산 값이 거대하다는 것
# (위에서도 적었 듯이 PCA는 분산값이 커야함)
# 고유 벡터는 결국 이 고유값들을 모아 놓은 벡터 형태가 되는데
# 데이터의 새로운 축을 나타내며 이 축을 따라 데이터가 가장 크게 분산됨
# 아주 신기한 현상인데 말로만 얘기하면 사실 이게 무슨 얘기인지 모를 수 있음
# 그래서 이에 대한 결과가 실제로 어떻게 반영되는 지를 봐야 하는데
# 기존에 그냥 어느 정도 밀집된 구조가 구상되었다면
# PCA를 수행하는 순간 이 값들이 아주 고르게 분산되어 퍼지는 것을 볼 수 있음
# 그럼에도 불구하고 재밌는 것은 데이터의 특성은 유지되고 있다는 것이기 때문에
# 정보들을 분류하고 파악하는 것에 아주 큰 도움이 됨
# 통계학을 학습할 때 Z Transform 이라는 것을 학습함
# 공업수학에서 배우는 Laplace Transform의 디지털 변환에 해당하는 Z Transform은 아님
# 말 그대로 Z 변환이라고 하는데 실제로 우리가 TensorFlow 및
# Scikit Learn을 사용하면서 많이 봤던 StandardScaler()가 바로 이 역할을 수행
# 평균이 0, 분산이 1이 되도록 표준화를 함
# 그래서 옛날 수학의 정책에 보면 뒤쪽에 통계학 쪽 도표가 그려져 있는 것을 볼 수 있는데
# 바로 그것을 만들어 주는 작업이 이 Z Transform(Z 변환)에 해당
# 실제 통계 책애서는 z score를 아래와 같이 나타냅니다.
# z = (x-mu) / sigma

principalComponentAnalysisRouter = APIRouter()


async def injectPrincipalComponentAnalysisService() -> PrincipalComponentAnalysisServiceImpl:
    return PrincipalComponentAnalysisServiceImpl()


@principalComponentAnalysisRouter.get("/pca-analysis")
async def principalComponentAnalysisTrain(principalComponentAnalysisService: PrincipalComponentAnalysisServiceImpl =
                                Depends(injectPrincipalComponentAnalysisService)):

    print(f"controller -> principalComponentAnalysisTrain()")

    originalData, pcaData, explainVarianceRatio = principalComponentAnalysisService.pcaAnalysis()

    return {
        "original_data": originalData,
        "pca_data": pcaData,
        "explained_variance_ratio": explainVarianceRatio
    }