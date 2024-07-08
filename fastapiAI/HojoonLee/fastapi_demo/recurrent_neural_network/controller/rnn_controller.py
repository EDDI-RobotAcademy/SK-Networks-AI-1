from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from recurrent_neural_network.service.rnn_service_impl import RecurrentNeuralNetworkServiceImpl

recurrentNeuralNetworkRouter = APIRouter()

async def injectRecurrentNeuralNetworkService() -> RecurrentNeuralNetworkServiceImpl:
    return RecurrentNeuralNetworkServiceImpl()

@recurrentNeuralNetworkRouter.post("/rnn-train")
async def rnnBasedTextTrain(recurrentNeuralNetworkService: RecurrentNeuralNetworkServiceImpl =
                            Depends(injectRecurrentNeuralNetworkService)):
    print(f"controller -> rnnBasedTextTrain()")

    recurrentNeuralNetworkService.trainText()

class RnnRequestForm(BaseModel):
    inputText: str

@recurrentNeuralNetworkRouter.post("/rnn-predict")
async def rnnBasedTextPredict(rnnRequestForm: RnnRequestForm,
                              recurrentNeuralNetworkService: RecurrentNeuralNetworkServiceImpl =
                              Depends(injectRecurrentNeuralNetworkService)):
    inputText = rnnRequestForm.inputText # unprocessable Entity 문제를 해결하기 위함
    print(f"inputText : {inputText}")
    if not inputText:
        raise HTTPException(status_code=400, detail='텍스트 입력을 해주세요!')
    print(f"controller -> rnnBasedTextPredict()")

    generatedText = recurrentNeuralNetworkService.predictText(inputText)
    return {"generatedText" : generatedText}
