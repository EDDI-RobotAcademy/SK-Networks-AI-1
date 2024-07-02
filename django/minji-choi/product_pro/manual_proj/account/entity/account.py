from django.db import models
from account.entity.account_login_type import AccountLoginType
from account.entity.account_role_type import AccountRoleType


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    # 실질적으로 AccountLoginType이 Account를 외래키로 가져가는 것이 더 좋음.
    # RoleType도 마찬가지이나 우선을 이렇게 진행
    # 또한 이것은 정해진 것이 아니며, 만드는 SW에 따라 유불리가 달라짐.
    # 고로 표현하려는 Domain이 어떤 Entity들이 존재하는 것이 파악하는 것이 중요함
    # 사용자의 블랙리스트의 처리를 빨리 하고 싶다면 외래키로 가져오는 것이 굿
    # 반면 특정 등급을 가지고 있는 회원들한테만 메일을 전송할 때는 Roletype이 acccount를 관리하는 것이 굿
    loginType = models.ForeignKey(AccountLoginType, on_delete=models.CASCADE)
    roleType = models.ForeignKey(AccountRoleType, on_delete=models.CASCADE)


    def __str__ (self):
        return f"Account -> id: {self.id}, loginType: {self.loginType}, roleType: {self.roleType}"


    class Meta:
        db_table = 'account'
        app_label = 'account'