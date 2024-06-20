from pydantic import BaseModel

# 일단 ResponseForm은 만들었음

class AnalysisResultResponseForm(BaseModel):
    accuracy: float
    confusion_matrix: list
    classification_report: dict