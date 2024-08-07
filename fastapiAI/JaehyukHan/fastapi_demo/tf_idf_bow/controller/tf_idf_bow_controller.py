from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from tf_idf_bow.controller.request_form.tf_idf_bow_request_form import TfIdfBowRequestForm
from tf_idf_bow.service.tf_idf_bow_service_impl import TfIdfBowServiceImpl

tfIdfBowRouter = APIRouter()

async def injectTfIdfBowService() -> TfIdfBowServiceImpl:
    return TfIdfBowServiceImpl()

# Term Frequency Inverse Document Frequency (TFIDF)
# 입력한 문장을 토대로 유사도가 높은 문장을 찾습니다.
# countVectorizer는 문서 벡터화에 사용되는 CountVectorizer 객체입니다.
# cosine_similarity()를 사용하여 messageVector와 countMatrix 사이의 유사도를 계산합니다.
# cos의 특성상 -1 ~ 1의 범주를 가지며 어차피 음수는 필요가 없으므로 0 ~ 1 사이의 값을 가지고 계산합니다.
# 특정 데이터가 (3, 5) 이고 (4, 4) 라고 하면 cos 각도 상의 차이가 발생합니다.
# 이를 토대로 유사도를 파악하는 시스템이라 보면 되겠습니다.
# 즉 기준을 대상으로 90도가 되면 연관이 없다 판정할 것입니다.
# 기준을 대상으로 0도가 되면 완벽하게 일치한다 판정할 것입니다.
# cos(0)과 cos(90)은 1과 0이기 때문입니다.
@tfIdfBowRouter.post("/find-similarity-document")
async def findSimilarityDocument(tfIdfBowRequestForm: TfIdfBowRequestForm,
                                 tfIdfBowService: TfIdfBowServiceImpl =
                                 Depends(injectTfIdfBowService)):
    print(f"controller -> findSimilarityDocument(): tfIdfBowRequestForm: {tfIdfBowRequestForm}")

    foundSimilarityDocumentList = tfIdfBowService.findSimilarDocumentList(tfIdfBowRequestForm.userSendMessage)
    return JSONResponse(content=foundSimilarityDocumentList, status_code=status.HTTP_200_OK)