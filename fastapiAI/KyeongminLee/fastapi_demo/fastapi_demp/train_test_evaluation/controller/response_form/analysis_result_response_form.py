from pydantic import BaseModel


class AnalysisResultResponseForm(BaseModel):
    accuracy: float
    confusion_matrix: list
    classification_report: dict