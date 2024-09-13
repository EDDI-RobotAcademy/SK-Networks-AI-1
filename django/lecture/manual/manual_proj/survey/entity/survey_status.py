from django.db import models
from django.utils.translation import gettext_lazy as _

class SurveyStatus(models.IntegerChoices):
    PENDING = 1, _('Pending')
    READY = 2, _('Ready')
