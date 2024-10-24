from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from typing import Optional, Union, Any, List
from pydantic import BaseModel

aiCommandRouter = APIRouter()


class AiRequestForm(BaseModel):
    userToken: str
    command: int
    data: Optional[Union[Any, List[Any]]] = None


@aiCommandRouter.post("/ai-request")
async def requestAiCommand(aiRequestForm: AiRequestForm):
    print(f"controller -> requestAiCommand(): aiRequestForm: {aiRequestForm.dict()}")

    return JSONResponse(content=True, status_code=status.HTTP_200_OK)
