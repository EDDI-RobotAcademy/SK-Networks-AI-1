from fastapi import APIRouter, Depends, HTTPException, status

from principal_component_analysis.service.pca_service_impl import PrincipalComponentAnalysisServiceImpl

principalComponentAnalysisRouter = APIRouter()

# PCA (Principal Component Analysis) 라는 주성분 분석이라는 이름을 가지고 있음
# 제일 중요한 특징이라면 고차원의 데이터를 분석 할 때 주요 특징들은 유지하면서
# 데이터를 저차원의 공간으로 보낼 수 있는 매우 훌륭한 기법입니다.

# 이게 무슨 개소리냐 ?
# 고차원의 데이터란 것은 결국 데이터를 판정할 때 사용하는 파라미터가 여러 개 있다는 뜻입니다.
# 쉽게 얘기해서 ax^n + bx^(n-1) + cx^(n-2) + cx^(n-3) + cx^(n-4) + ... + zzz^(n-1004) + ... +
# 위와 같은 형태로 표현 되는 케이스를 좀 더 단순화 시켜서 유사한 혹은 동일한 모양을 만들어내는 것이죠.
# 위 케이스는 결국 n 차원이지만 PCA를 통해서 이 n 차원을 n - x 차원으로 떨굴 수 있다는 것이 핵심입니다.
# 설명을 위해 2차원으로 했지만 3차원, 4차원 등등 관여하는 종속 변수가 더 많을 수 있습니다.

# 실제로 PCA 분석은 분산 (Variance) 를 최대화 하는 축(Principal Component)를 찾는 것이 핵심입니다.
# Principal Component Analysis 라고 이름 붙은 이유가
# 결국 분산을 최대화하는 주성분을 찾아 분석하는 기법이기 때문입니다.
# PCA는 결국 분산값을 최대화하는 새로운 좌표계를 생성하게 됩니다.

# 이렇게 여러 종속 변수들이 존재하는 영역에서 반드시 다뤄지는 것이 있는데
# 바로 공분산이라는 Co-Variance 라는 녀석입니다.
# 실제로 PCA는 공분산 행렬을 사용하여 데이터의 분산과 상관 관계를 분석합니다.
# 공분산 행렬의 고유값(eigenvalue)과 고유벡터(eigenvector)를 계산하여 데이터 주성분을 찾습니다.
# 학교에서 Linear Algebra(선형대수) 학습 할 때 고유값, 고유벡터는 많이들 들어보셨을 것입니다.
# 피보나치 수열의 일반화를 위해서도 고유값과 고유벡터를 사용하니까요.

# 여기서 고유값이 크고 작은 것은 상당히 중요한 척도가 됩니다.
# 고유값이 크면 클수록 해당 벡터 방향으로의 분산 값이 거대하다는 것입니다.
# (위에도 적었듯이 PCA는 분산값이 커야합니다)
# 고유 벡터는 결국 이 고유값들을 모아놓은 벡터 형태가 되는데
# 데이터의 새로운 축을 나타내며 이 축을 따라 데이터가 가장 크게 분산됩니다.
# 아주 신기한 현상인데 입으로만 얘기하면 사실 이게 무슨 얘기지 할 수 있습니다.
# 그래서 이에 대한 결과가 실제로 어떻게 반영되는지를 봐야 하는데
# 기존에 그냥 어느정도 밀집된 구조가 구성되었다면
# PCA를 수행하는 순간 이 값들이 아주 고르게 분산되어 퍼지는 것을 볼 수 있습니다.
# 그럼에도 불구하고 재밌는 것은 데이터의 특성은 유지되고 있다는 것이기 때문에
# 정보들을 분류하고 파악하는 것에 아주 큰 도움이 됩니다.

# 통계학을 학습 할 때 Z Transform 이라는 것을 학습합니다.
# 공업수학에서 배우는 Laplace Transform의 디지털 변환에 해당하는 Z Transform은 아닙니다.
# 말 그대로 Z 변환이라고 하는데 실제로 우리가 TensorFlow 및
# Scikit Learn을 사용하면서 많이 봤던 StandardScaler() 가 바로 이 역할을 수행합니다.
# 평균이 0, 분산이 1이 되도록 표준화합니다.
# 그래서 옛날 수학의 정책에 보면 뒤쪽에 통계학쪽 도표가 그려져 있는 것을 볼 수 있는데
# 바로 그것을 만들어주는 작업이 이 Z Transform(Z 변환)에 해당합니다.

# 실제 통계 책에서는 z score를 아래와 같이 나타냅니다.
# z = (x - 뮤) / 시그마
# 뮤는 포켓몬 뮤 아님
# 뮤는 평균값을 의미하며 x는 각 데이터의 샘플임
# 그리고 시그마는 표준 편차(Standard Deviation)에 해당합니다
# 분산에 루트를 씌우면 표준 편차가 됩니다.

# 분산을 구하는 방법이라면
# (x - 뮤)^2 / 샘플개수

# 우선 대략 이러한 흐름을 잡고 PCA 분석을 살펴보면 이게 뭐하는 짓인지 대략은 파악할 수 있음
# 결론적으로 종속 변수가 너무 많아서 '정신 나가겠다' 할 때 사용하면 좋다.

async def injectPrincipalComponentAnalysisService() -> PrincipalComponentAnalysisServiceImpl:
    return PrincipalComponentAnalysisServiceImpl()


@principalComponentAnalysisRouter.get("/pca-analysis")
async def pcaAnalysis(principalComponentAnalysisService: PrincipalComponentAnalysisServiceImpl =
                      Depends(injectPrincipalComponentAnalysisService)):

    print(f"controller -> pcaAnalysis()")

    originalData, pcaData, explainedVarianceRatio = principalComponentAnalysisService.pcaAnalysis()

    return {
        "original_data": originalData,
        "pca_data": pcaData,
        "explained_variance_ratio": explainedVarianceRatio,
    }
    