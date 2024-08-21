from typing import List
from pydantic import BaseModel


class OpenAIPaperSimilarityAnalysisRequestForm(BaseModel):
    paperTitleList: List[str]
    userRequestPaperTitle: str
