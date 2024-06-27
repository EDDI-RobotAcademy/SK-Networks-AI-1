from django.db import models


class AccountRoleType(models.Model):
    # 64 선택의 이유: OS가 내부적으로 메모리 관리를 64 * 2^n 단위로 관리하기 때문
    roleType = models.CharField(max_length=64)

    def __str__(self):
        return self.roleType

    class Meta:
        db_table = 'account_role_type'
        app_label = 'account'