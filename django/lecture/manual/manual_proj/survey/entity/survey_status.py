from django.db import models

class SurveyStatus(models.IntegerChoices):
    PENDING = 1, 'Pending'
    ACTIVE = 2, 'Active'
    CLOSED = 3, 'Closed'
