from langchain.chains.llm import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from fastapi import APIRouter, status

from fastapi.responses import JSONResponse
from pydantic import BaseModel


cotRouter = APIRouter()

class CotRequestForm(BaseModel):
    userSendQuestion: str

@cotRouter.post("/cot-based-question")
async def answerWithCoT(cotRequestForm: CotRequestForm):

    print(f"controller -> answerWithCoT(): cotRequestForm: {cotRequestForm}")

    cot_prompt = PromptTemplate(
        input_variables=["question"],
        template="""
        넌 복잡한 문제를 단계별로 논리적으로 해결하는 AI 전문가다.
        너에게 주어진 질문에 대해 올바른 답을 도출하기 위해 자세하고 논리적인 추론 과정을 사용해라
        
        질문: {question}
        
        논리적 추론 과정"""
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
    cot_chain = LLMChain(llm=llm, prompt=cot_prompt)
    response = cot_chain.run(cotRequestForm.userSendQuestion)

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)