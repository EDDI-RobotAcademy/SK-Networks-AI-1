from django.db import models
from account.entity.account import Account


class Profile(models.Model):
    ## 주의할 점 : DB의 유일성이 꺠지면 검색한는 상황에서 요상한 일이 발생한다
    # 일단 프로필 사진은 생략
    nickname = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=64, unique=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE) # 1:1 맵핑



    def __str__(self):
        return f"Profile -> email: {self.email} ,nickname: {self.nickname}"

    class Meta:
        db_table = 'profile'
        app_label = 'account'