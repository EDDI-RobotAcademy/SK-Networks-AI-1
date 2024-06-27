from fastapi import APIRouter
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

from kmeans.controller.response_form.kmeans_cluster_response_form import KmeansClusterResponseForm

kmeansRouter = APIRouter()

@kmeansRouter.get("/kmeans-test", response_model=KmeansClusterResponseForm)
async def kmeans_cluster_anaylysis():
    # Scikit Learn 에서 제공하는 Kmeans Cluster를 생서하는 라이브러리
    # 300개의 샘플 데이터를 생성함
    # 4개의 중앙값을 구성함
    # 클러스터(중앙값) 기준의 Standard Deviation(표준편차)는 0.60
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

    # 위의 것은 그냥 임의로 4개의 군집 데이터를 만든 것
    # 4개의 클러스터로 데이터를 군집화
    # 서로 다른 중심값을 가지고 알고리즘을 10번 돌려봄
    # 그 중 가장 성능 지표가 좋은 것을 채택함
    # 여기서 성능 지표는 중심점으로부터 데이터들이 떨어진 거리값을 의미함
    # 데이터가 분포된 공간이 2차원이라면 sqrt(x^2 + y^2) <- 피타고라스
    # 3차원이라면 sqrt(x^2 + y^2 + z^2) <- 피타고라스 동일
    # 거리값이 짧으면 짧을수록 성능 지표가 우수한 것임
    kmeans = KMeans(n_clusters=4, n_init=10)
    kmeans.fit(X)

    labels = kmeans.labels_.tolist()
    centers = kmeans.cluster_centers_.tolist()
    points = X.tolist()
    print(f"points: {points}, labels; {labels}, centers: {centers}")

    # 위의 Response Model을 지정한면 아래와 같이 구성할 수도 있음
    # 그러나 별로 권장하고 싶은 방식은 아님
    # 시스템이 커지고 Domain이 복잡해질수록 '뭐지?' 싶은 것들이 증대하게 됨
    # 그러나 세상에서 다양한 사람들ㅇ르 만날 수 있으니 알아둘 필요는 있음
    return {"centers": centers, "labels": labels, "points": points}