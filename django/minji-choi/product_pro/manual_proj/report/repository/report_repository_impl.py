from report.repository.report_repository import ReportRepository

from report.entity.report import Report


class ReportRepositoryImpl(ReportRepository):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def findByAccount(self, account):
        try:
            report = Report.objects.get(account=account)
            return report
        except Report.DoesNotExist:
            print('report is None.')
            return None

    def register(self, account, age, gender):
        print('서베이 레포트 만들기')
        report = Report.objects.create(account=account, age=age, gender=gender)