from fastapi import APIRouter, Depends

from decision_tree.service.decision_tree_service_impl import DecisionTreeServiceImpl

decisionTreeRouter = APIRouter()


async def injectDecisionTreeSerivce() -> DecisionTreeServiceImpl:
    return DecisionTreeServiceImpl()


@decisionTreeRouter.get('/decision-tree-train')
async def decisionTreeTrain(decisionTreeService: DecisionTreeServiceImpl =
                            Depends(injectDecisionTreeSerivce)):
    print(f'controller -> decisionTreeTrain()')

    decisionTreeService.decisionTreeTrain()
