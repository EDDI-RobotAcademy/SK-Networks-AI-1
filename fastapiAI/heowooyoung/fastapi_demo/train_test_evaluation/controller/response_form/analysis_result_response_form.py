from pydantic import BaseModel


# 일단 ResponseForm은 만들었음
# 근데 '솔까 왜 만드는지 모르겠음' 라고 생각할 수 있음
# 실질적으로 Domain이 협력하는 상황에 대해서도 고민해 볼 필요가 있음
# 당장 여기서는 그냥 다 랜덤이고 존재하는 데이터 가지고 하기 때문에 그냥 효용을 못느낄 수 있음
# 그러나 order 만 생각해봐도 벌써 account와 product와 연동하고 있음
# 이런 경우 order 정보만 주는게 아니라 
# 경우에 따라서 account와 product 정보의 일부를 추출해서 줘야할 수 있음
# 그럼 '어떻게 줄 것이냐 ?' 라는 문제에 봉착하게 됨

# 퉁치는 경우를 생각해보자
# 전부 다 하나에 때려박은 다음에 보냈다.
# 근데 새로운 비즈니스 및 마켓팅에 의해 보내줘야 하는 정보의 내용이 추가되었다.
# 혹은 일부는 빼내야하고 버려야한다.
# 재밌게도 마켓팅이란 것이 이것도 해보고 저것도 해보고 사람들 반응도 보고 하나 보면
# 결이 딱 정해져 있는 것이 아니라 이것 저것 해보면서 데이터도 이것 저것 들어가게 됨
# 그러다 보니 사실 변경이 매우 빈번하게 발생함
# 근데 실질적으로 모든 기능들이 다 엮여 있다보니 저런 변경 상황에 유연성을 잃어버리게 됨
# 고로 다 분리하자라는 관점에서 Response, ResponseForm, Request, RequestForm이 만들어짐

# 여기서도 Response와 ResponseForm이 나뉘어지는데
# 보편적으로 Response는 특정 Domain 정보를 추출하기 위한 목적으로 사용함
# 고로 'ResponseForm은 도대체 무엇이냐 ?' 라는 의문이 여전히 남음

# 실제로 우리가 데이터를 보는 장소는 웹 페이지 입니다.
# 그렇기 때문에 웹 페이지에서 보여주고자 하는 Format(형식)이 존재합니다.
# 바로 이 형식에 맞춰주는 것이 ResponseForm 입니다.

# 반대로 RequestForm의 경우도 있는데
# 웹 페이지에서 보내는 정보가 특정 Domain에 국한 된 것이 아니라
# 여러 Domain 정보가 한 번에 몰려 들어올 수 있기 때문입니다.
# 대표적으로 주문(Order)라는 것이 역시 그러합니다.
# 주문 시 주문과 관련한 정보로 주문 번호, 주문 고객,
# 주문 상품, 결제 금액, 배송 관련 등등의 정보들이 전부 결합 될 수 밖에 없습니다.
# 이런 상황에서 각 Domain 별로 Request와 Response를 관리하려면
# 전체를 묶고 필요에 따라 특정 Domain의
# Response, Request 전환이 가능하도록 구성하는 것이
# 코드의 가독성과 변경에 대한 유연성이 더욱 강화됩니다.

# 이전에도 적었듯이 이런 작업들이 많아지면
# DTO도 좀 불편해지기 때문에 응답과 요청을 나눕니다.
class AnalysisResultResponseForm(BaseModel):
    accuracy: float
    confusion_matrix: list
    classification_report: dict
