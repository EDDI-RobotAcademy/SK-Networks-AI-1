from django.db import models

from account.entity.account import Account


class Profile(models.Model):
    # 주의 바람 -> DB의 유일성이 깨지면 검색하는 상황에서 요상한 일이 발생할 수도 있음
    nickname = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile -> email: {self.email}, nickname: {self.nickname}"

    class Meta:
        db_table = 'profile'
        app_label = 'account'