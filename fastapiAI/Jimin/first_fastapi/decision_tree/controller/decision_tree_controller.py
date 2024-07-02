from fastapi import APIRouter, Depends, status

from decision_tree.service.decision_tree_service_impl import DecisionTreeServiceImpl

decisionTreeRouter = APIRouter()

async def injectDecisionTreeService() -> DecisionTreeServiceImpl:
    return DecisionTreeServiceImpl()


@decisionTreeRouter.get("/decision-tree-train")
async def decisionTreeTrain(decisionTreeService: DecisionTreeServiceImpl = Depends(injectDecisionTreeService)):
    print(f"controller -> decisionTreeTrain()")

    decisionTreeService.decisionTreeTrain()

