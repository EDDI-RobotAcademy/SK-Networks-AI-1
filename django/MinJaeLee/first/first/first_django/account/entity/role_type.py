from django.db import models


class RoleType(models.TextChoices):
    ADMIN = 'ADMIN'
    NORMAL = 'NORMAL'
    BLACKLIST = 'BLACKLIST'
