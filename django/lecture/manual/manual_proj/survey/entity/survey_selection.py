from django.db import models
from .survey_question import SurveyQuestion

class SurveySelection(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(SurveyQuestion, related_name='selections', on_delete=models.CASCADE)
    selection_text = models.CharField(max_length=255)

    def __str__(self):
        return self.selection_text

    class Meta:
        db_table = 'survey_selection'
        app_label = 'survey'
