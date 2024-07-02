from fastapi import APIRouter
from fastapi.responses import JSONResponse

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from kmeans.controller.response_form.kmeans_cluster_response_form import KmeansClusterResponseForm

kmeansRouter = APIRouter()
# kmeans는 사용이 단순한 것에 비해 활용을 닿
@kmeansRouter.get("/kmeans-test", response_model=KmeansClusterResponseForm)
def kmeans_cluster_analysis():
    print("kmeans_cluster_analysis()")
    # Scikit learn에서 제공하는 Kmeans cluster를 생성하는 라이브러리
    # 300개의 샘플 데이터 생성, 4개의 중앙값 구성, 클러스터(중앙값) 기준의 standard deviation(표편)은 0.6, 재현율 만땅
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
    kmeans = KMeans(n_clusters=4, n_init=10)
    kmeans.fit(X)

    labels = kmeans.labels_.tolist()
    centers = kmeans.cluster_centers_.tolist()
    points = X.tolist()
    print(f"points: {points}, labels: {labels}, centers: {centers}")
    # 위의 Response Model을 지정하면 아래와 같이 구성할 수도 있음
    # 그러나 별로 권장하고 싶은 방식은 아님
    # 시스템이 커지고 도메인이 복잡해질수록 이상해짐, 그러나 세상에서 다양한 사람들을 만날 수 있으니 알긴 해야함
    return {"centers":centers, "labels":labels, "points":points}

