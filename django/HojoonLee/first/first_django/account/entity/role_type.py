from django.db import models
class RoleType(models.Model):
    ADMIN = 'ADMIN'
    NORMAL = 'NORMAL'
    BLACKLIST = 'BLACKLIST'
    # 여기까지만 구현하면 사용자 정보를 모름 >> 프로필이 필요 >> profile.py 구현
    # 여기는 단순 ENUM의 느낌이라 aggregate 시키지는 않음


