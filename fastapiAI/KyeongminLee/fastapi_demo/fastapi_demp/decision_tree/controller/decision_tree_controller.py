from fastapi import APIRouter, Depends, HTTPException, status

from decision_tree.service.decision_tree_service_impl import DecisionTreeServcieImpl

decisionTreeRouter = APIRouter()


async def injectDecisionTreeService() -> DecisionTreeServcieImpl:
    return DecisionTreeServcieImpl()


@decisionTreeRouter.get("/decision-tree-train")
async def decisionTreeTrain(decisionTreeService: DecisionTreeServcieImpl =
                               Depends(injectDecisionTreeService)):

    print(f"controller -> decisionTreeTrain()")
    decisionTreeService.decisionTreeTrain()