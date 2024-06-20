from pydantic import BaseModel

# 일단 ResponseForm은 만들었음
# 근데 왜 만드냐?
# 실질적으로 Domain이 협력하는 상황에 대해서도 고민해 볼 필요가 있음
# 당장 여기서는 그냥 다 랜덤이고 존해나는 데이터 가지고 하기 때문에 그냥 효용을 못 느낄 수 있음
# 그러나 order만 생각해봐도 벌서 account와 product와 연동하고 있음
# 이런 경우 order 정보만 주는게 아니라 경우에 따라서 account와 product 정보의 일부를 추출해서 줘야할 수 있음
# 그럼 어떻게 줄것이냐?

# Response, ResponseFrom, Request, RequestForm
# Response는 특정 Domain 정보를 추출하기 위한 목적으로 사용함
# 실제 우리가 데이터를 보는 장소는 웹 페이지
# 웹페이지에서 보여주고자 하는 Format(형식)에 맞춰주는 것이 ResponseForm

# 반대로 RequestForm은 웹페이지에서 보내는 정보가 특정 Domain에 국한 된 것이 아니라 여러 Domain 정보가 한번에 몰려 들어올 때 형식
# 대표적으로 주문(order) 시 주문과 관련한 정보로 주문 번호, 주문 고객, 금액, 배송 등등의 정보들이 전부 결합
# 이런 상황에서 각 Domain별로 Request와 Response를 관리하려면 전체를 묶고 필요에 따라 특정 Domain의 Response와 Request 전환이 가능하도록
# 작업들이 많아지면 응답과 요청을 나눈다.
class AnalysisResultResponseForm(BaseModel):
    accuracy: float
    confusion_matrix: list
    classification_report: dict