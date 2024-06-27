from fastapi import APIRouter
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

from kmeans.controller.response_form.kmeans_cluster_response_form import KmeansClusterResponseForm

kmeansRouter = APIRouter()


@kmeansRouter.get("/kmeans-test", response_model=KmeansClusterResponseForm)
async def kmeans_cluster_analysis():
    X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

    kmeans = KMeans(n_clusters=4, n_init=10)
    kmeans.fit(X)

    labels = kmeans.labels_.tolist()
    centers = kmeans.cluster_centers_.tolist()
    points = X.tolist()
    print(f"points: {points}, labels: {labels}, centers: {centers}")
    return {"centers": centers, "labels": labels, "points": points}
