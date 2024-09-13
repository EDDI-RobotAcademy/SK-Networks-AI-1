from django.db import models
from django.utils.translation import gettext_lazy as _

class SurveyType(models.TextChoices):
    GENERAL = 1, _('General')
    FIVE_SCORE = 2, _('Five Score')
    BOOLEAN = 3, _('Boolean')
