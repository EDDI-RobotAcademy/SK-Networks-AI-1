from django.db import models
class AccountLoginType(models.Model):

    class LoginType(models.TextChoices):
        KAKAO = 'KAKAO', 'kakao' # 현재는 카카오만 하므로 얘만

    loginType = models.CharField(max_length=10, choices=LoginType.choices)

    def __str__(self):
        return self.loginType

    class Meta:
            db_table = 'account_login_type'
            app_label = 'account' # 이렇게 함으로써 account aggregated root가 됨
            # aggregated root 를 해주는 기준? : 해당 도메인(account)을 잘 표현해 줄 수 있는가? (서비스를 하는 측면에서 고려)