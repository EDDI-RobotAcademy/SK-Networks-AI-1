from io import BytesIO

from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
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

    return JSONResponse(content={'status': "모델 훈련 및 저장이 완료되었습니다!"})


@convolutionNeuralNetworkRouter.post("/cnn-predict")
async def cnnBasedImagePredict(file: UploadFile = File(...),
                               convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl =
                               Depends(injectConvolutionNeuralNetworkService)):
    print("controller -> cnnBasedImagePredict()")
    try:
        file = await file.read()
        predictedClass = convolutionNeuralNetworkService.imagePredict(file)
        return JSONResponse(content={"predictedClass": predictedClass})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"잘못된 형식으로 요청을 보냈습니다: { e }")

@convolutionNeuralNetworkRouter.post("/cnn-evaluate")
async def cnnModelEvaluate(convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl =
                               Depends(injectConvolutionNeuralNetworkService)):

    print("controller -> cnnModelEvaluate()")

    evaluatedPerformance = convolutionNeuralNetworkService.modelEvaluate()

    return JSONResponse(content=evaluatedPerformance, status_code=status.HTTP_200_OK)