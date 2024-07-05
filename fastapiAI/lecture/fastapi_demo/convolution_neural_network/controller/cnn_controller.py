from fastapi import APIRouter, Depends, HTTPException, status

from convolution_neural_network.service.cnn_service_impl import ConvolutionNeuralNetworkServiceImpl

convolutionNeuralNetworkRouter = APIRouter()

async def injectConvolutionNeuralNetworkService() -> ConvolutionNeuralNetworkServiceImpl:
    return ConvolutionNeuralNetworkServiceImpl()


@convolutionNeuralNetworkRouter.post("/cnn-train")
async def cnnBasedImageTrain(convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl =
                             Depends(injectConvolutionNeuralNetworkService)):

    print(f"controller -> cnnBasedImageTrain()")

    convolutionNeuralNetworkService.imageTrain()
