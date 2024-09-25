from django.db import models

from survey.entity.survey_status import SurveyStatus


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.IntegerField(
        choices=SurveyStatus.choices,
        default=SurveyStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'survey'
        app_label = 'survey'
