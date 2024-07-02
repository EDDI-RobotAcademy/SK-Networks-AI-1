from sklearn.datasets import load_wine

from decision_tree.repository.decison_tree_repository import DecisionTreeRepository


class DecisionTreeRepositoryImpl(DecisionTreeRepository):

    def loadWineInfo(self):
        return load_wine()
