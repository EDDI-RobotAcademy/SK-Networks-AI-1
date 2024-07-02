from decision_tree.repository.decison_tree_repository_impl import DecisionTreeRepositoryImpl
from decision_tree.service.decision_tree_service import DecisionTreeService


class DecisionTreeServiceImpl(DecisionTreeService):

    def __init__(self):
        self.decisionTreeRepository = DecisionTreeRepositoryImpl()

    def decisionTreeTrain(self):
        print("service -> decisionTreeTrain()")

        wineInfo = self.decisionTreeRepository.loadWineInfo()
        print(f'wine feature names: {wineInfo.feature_names}')