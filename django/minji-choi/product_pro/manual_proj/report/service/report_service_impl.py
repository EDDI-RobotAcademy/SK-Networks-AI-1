from account.repository.account_repository_impl import AccountRepositoryImpl
from report.repository.report_repository_impl import ReportRepositoryImpl
from report.service.report_service import ReportService

class ReportServiceImpl(ReportService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__reportRepository = ReportRepositoryImpl.getInstance()

        return cls.__instance
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createReport(self, age, gender, accountId):
        account = self.__accountRepository.findById(accountId)  # 있음
        report = self.__reportRepository.findByAccount(account)
        if report is None:
            report = self.__reportRepository.register(account, age, gender)
        # print('이미 있는 report')