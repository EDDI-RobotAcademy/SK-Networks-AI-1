from fastapi import APIRouter
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

from kmeans.controller.response_form.kmeans_cluster_response_form import KmeansClusterResponseForm

kmeansRouter = APIRouter()

# kmeans는 사용은 단순한데 비해 활용을 굉장히 다방면으로 할 수 있어서 좋은 녀석
# 우선 범용적으로 영화 장르를 분석할 때
# 멜로 영화, 액션 영돠, 공포 영화 같은 것이 있다고 해봅시다.
# 10대들이 무엇에 가장 관심을 가지느가라고 단순하게 판정할 것이 아닌
# 각각의 구성원들의 취향이 있기 때문에
# 이런 경우 특정 사람들을 그룹핑 해주는 것이 바로 kmeans cluster  알고리즘입니다.
# 취향 분석에 사용할 수 있다는 의미.

# 그리고 별개로 군사적 목적으로 사용할 수도 있음
# 대표적인 예가 LRASM 미사일임
# 보편적으로 미사일로 정밀 타격을 할 때 군사용 위성을 사용하여 유도함
# 그런데 요즘 전자전이 발달하다보니 통신 신호를 교란시킬 수 있음
# 그래서 GPS 신호를 교란하는 교ㅛ란기들을 보편적인 항모전달으로 운용을 함
# 그런데도 싸워야 하니까 이것을 우회할 방법으로 인공지능을 채틱하였음
# GPS 재밍 지녁에서는 미사일에 탑재된 전자파로 상대 전단의 레이더 신호를 감지함
# 그리고 사거리 밖으로 자동 라우팅 플랜을 세움
# 그렇게 레이더에 감지되지 않는 거리 밖으로 이동함
# 이후 전자파에 잡히는 데이터들을 그룹핑함 (이 때 kmeans cluster를 사용함)
# 그리고 타격해야 하는 목표물이 무엇인지 id를 부여해서 간파하기 시작함
# kmeasn cluster에 의해 타겟이 확보되면 급강하를 진행함
# 저공 비행을 하면 보편적으로 레이더에 잘 안걸리게 됨
# 그리고 알려가서 때려박음

# 이 당시 록히드 마틴에서 LRASM 미사일을 발표하고 곰돌이 푸가 화냈음
# 사실 요런 것을 보면 인공지능이 가장 많이 활용되는 분야가 군사 분야라는 것도 알 수 있음.
# 생각보다 요즘 한국 방산의 위력이 어마어마함

@kmeansRouter.get('/kmeans-test', response_model = KmeansClusterResponseForm)
async def kmeans_cluster_analysis():
    # Scikit-learn에서 제공하는 Kmeans Cluster를 생성하는 라이브러리
    # 300개의 샘플 데이터를 생성함
    # 4개의 중앙값을 구성함
    # 클러스터 기준의 Standard Deviation는 0.60
    # 재현율 만땅
    X, _ = make_blobs(n_samples = 300, centers = 4, cluster_std = 0.60, random_state = 0)


    # 위의 것은 그냥 임의로 4개의 군집 데이터를 만든 것
    # 4개의 클러스터로 데이터를 군집화
    # 서로 다른 중심 값을 가지고 알고리즘을 10번 돌려봄
    # 그 중 가장 성능 지표가 좋은 것을 태책함
    # 여기서 성능 지표는 중심점으로부터 데이터들이 떨어진 거리 값을 의미함
    # 데이터가 분포된 공간이 2차원이라면 sqrt(x^2 + y^2)
    # 거리 갑싱 짧으면 짧을수록 성능 지표가 우수한 것임

    kmeans = KMeans(n_clusters = 4, n_init = 10)
    kmeans.fit(X)

    labels = kmeans.labels_.tolist()
    centers = kmeans.cluster_centers_.tolist()
    points = X.tolist()
    # print(f"points: {points}, labels: {labels}, centers: {centers}")

    # 위의 Response Model을 지정하면 아래와 같이 구성할 수도 있음
    # 그러나 별로 권장하고 싶은 방식은 아님
    # 시스템이 커지고 Domain이 복잡해질수록 뭐지? 싶은 것들이 증대하게 됨
    # 그러나 세상에서 다양한 사람들을 만날 수 있으니 알아둘 필요는 있음
    return {'centers': centers, 'labels': labels, 'points': points}