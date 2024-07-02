from django.db import models

# enum 파일. 장고가 enum을 인식하지 못해서 class로 구현한 것. 주사위 1~6 같은 것
class RoleType(models.TextChoices):
    ADMIN = 'ADMIN' # 관리자
    NORMAL = 'NORMAL' #사용자
    BLACKLIST = 'BLACKLIST'