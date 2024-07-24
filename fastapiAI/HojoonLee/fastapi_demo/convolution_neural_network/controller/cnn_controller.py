from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse
from convolution_neural_network.service.cnn_service_impl import ConvolutionNeuralNetworkServiceImpl

ConvolutionNeuralNetworkRouter = APIRouter()

async def injectConvolutionNeuralNetworkService() -> ConvolutionNeuralNetworkServiceImpl:
    return ConvolutionNeuralNetworkServiceImpl()

@ConvolutionNeuralNetworkRouter.post("/cnn-train")
async def cnnBasedImageTrain(convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl =
                             Depends(injectConvolutionNeuralNetworkService)):
    print(f"controller -> cnnBasedImageTrain()")

    convolutionNeuralNetworkService.imageTrain()

    return JSONResponse(content={"status": "모델 훈련 및 저장이 완료 되었습니다."})

@ConvolutionNeuralNetworkRouter.post("/cnn-predict")
async def cnnBasedImagePredict(file: UploadFile = File(...),
                             convolutionNeuralNetworkService: ConvolutionNeuralNetworkServiceImpl =
                             Depends(injectConvolutionNeuralNetworkService)):
    try:
        # 이미지 파일을 받아와서 예측
        file = await file.read() # async하고 여기 await하면 bad request, async 지워져도 bad request
        predictedClass = convolutionNeuralNetworkService.imagePredict(file)
        return JSONResponse(content={"predictedClass": predictedClass})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"잘못된 형식으로 요청을 보냈습니다: {e}")