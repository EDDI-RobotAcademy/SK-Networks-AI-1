from django.db import models

from account.entity.account import Account


class Profile(models.Model):
    # 주의 바람 > DB의 유일성이 깨지면 검색하는 상황에서 요상한 일이 발생할 수 있음 => unique=True 하는 이유
    nickname = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    # account와 profile은 one to one 매칭 -> 1대1 매칭 -> db one to one 참고.. (유일하게 만들겠다는 명시임)
    account = models.OneToOneField(Account, on_delete=models.CASCADE) # Account 계정 날아가면 account도 날아간다

    def __str__(self):
        return f"Profile -> nickname: {self.nickname}, email: {self.email}"

    class Meta:
        db_table = 'profile'
        app_label = 'account'