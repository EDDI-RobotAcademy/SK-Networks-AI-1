from django.db import models


class RoleType(models.Model):
    ADMIN = 'ADMIN',
    NORMAL = 'NORMAL'
    BLACKLIST = 'BLACKLIST'