from pydantic import BaseModel


# 리스폰스 리스폰스폼 리퀘스트 리퀘스트폼 다 분리했음
# 리스폰스프롬이 무엇이냐?
# 웹페이지에 정보를 보여줄건데 이 형식이 폼멧이고 리스폰스폼 으로맞춰시킴
# 반대로 리퀘스트폼은 주문자의다양한정보가결합되서 필요하다는듯
class AnalysisResultResponseForm(BaseModel):
    accuracy: float
    confusion_matrix: list
    classification_report: dict