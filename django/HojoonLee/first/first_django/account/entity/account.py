from django.db import models

from account.entity.account_login_type import AccountLoginType
from account.entity.account_role_type import AccountRoleType


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    # 실질적으로 AccountLoginType이 Account를 ForeignKey로 가져가는 것이 더 좋음
    # 아래의 AccountRoleType도 마찬가지이나 우선은 이렇게 진행
    # 또한 이것은 정해진 것이 아니며 만드는 SW에 따라 유불리가 달라질 수 있음
    # 고로 표현하려는 Domain에 어떤 Entity들이 존재하는지 파악하는 것이 중요함
    loginType = models.ForeignKey(AccountLoginType, on_delete=models.CASCADE) # model 바뀔 때 마다 사라진다.
    roleType = models.ForeignKey(AccountRoleType, on_delete=models.CASCADE) # 관리자냐? 블랙리스트냐? 여부

    def __str__(self):
        return f"Account -> id: {self.id}, loginType:{self.loginType}, roleType:{self.roleType}"

    class Meta:
        db_table = 'account'
        app_label = 'account' # entity가 여럿이기 때문에 이것을 선언