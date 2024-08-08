import io

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from fastapi.responses import JSONResponse

from convolution_neural_network.service.cnn_service_impl import ConvolutionNeuralNetworkServiceImpl

convolutionNeuralNetworkRouter = APIRouter()


async def injectConvolutionNeuralNetworkService() -> ConvolutionNeuralNetworkServiceImpl:
    return ConvolutionNeuralNetworkServiceImpl()


@convolutionNeuralNetworkRouter.post("/cnn-train")
async def cnnBasedImageTrain(convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl = Depends(
    injectConvolutionNeuralNetworkService)):
    print(f"controller -> cnnBasedImageTrain()")

    convolutionNeuralNetworkService.imageTrain()


@convolutionNeuralNetworkRouter.post("/cnn-predict")
async def cnnBasedImagePredict(file: UploadFile = File(...),
                               convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl =
                               Depends(injectConvolutionNeuralNetworkService)):
    try:
        print('controller -> cnnBasedImagePredict()')
        file = await file.read()
        predictedClass = await convolutionNeuralNetworkService.imagePredict(file)
        return JSONResponse(content={"predictedClass": predictedClass})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"잘못된 형식으로 요청을 보냈습니다: {e}")


@convolutionNeuralNetworkRouter.post("/cnn-evaluate")
async def cnnModelEvaluate(convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl = Depends(
    injectConvolutionNeuralNetworkService)):
    print(f"controller -> cnnModelEvaluate()")

    evaluatedPrefomance = convolutionNeuralNetworkService.modelEvaluate()

    return JSONResponse(content=evaluatedPrefomance, status_code=status.HTTP_200_OK)
