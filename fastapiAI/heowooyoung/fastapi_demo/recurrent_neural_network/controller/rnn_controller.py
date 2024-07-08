from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse

from recurrent_neural_network.service.rnn_service_impl import RecurrentNeuralNetworkServiceImpl

recurrentNeuralNetworkRouter = APIRouter()

async def injectRecurrentNeuralNetworkService() -> RecurrentNeuralNetworkServiceImpl:
    return RecurrentNeuralNetworkServiceImpl()


@recurrentNeuralNetworkRouter.post("/rnn-train")
async def rnnBasedTextTrain(recurrentNeuralNetworkService: RecurrentNeuralNetworkServiceImpl =
                            Depends(injectRecurrentNeuralNetworkService)):

    print(f"controller -> rnnBasedTextTrain()")

    recurrentNeuralNetworkService.trainText()