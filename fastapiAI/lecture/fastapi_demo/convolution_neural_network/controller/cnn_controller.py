from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from convolution_neural_network.service.cnn_service_impl import ConvolutionNeuralNetworkServiceImpl

convolutionNeuralNetworkRouter = APIRouter()

async def injectConvolutionNeuralNetworkService() -> ConvolutionNeuralNetworkServiceImpl:
    return ConvolutionNeuralNetworkServiceImpl()


@convolutionNeuralNetworkRouter.post("/cnn-train")
async def cnnBasedImageTrain(convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl =
                             Depends(injectConvolutionNeuralNetworkService)):

    print(f"controller -> cnnBasedImageTrain()")

    convolutionNeuralNetworkService.imageTrain()

    return JSONResponse(content={"status": "모델 훈련 및 저장이 완료되었습니다!"})
