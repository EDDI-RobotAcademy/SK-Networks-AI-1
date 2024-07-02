from abc import ABC, abstractmethod

class ReportService(ABC):
    @abstractmethod
    def createReport(self, age, gender, accountId):
        pass