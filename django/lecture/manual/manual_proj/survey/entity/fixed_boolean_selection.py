from django.db import models
from .survey_question import SurveyQuestion

class FixedBooleanSelection(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(SurveyQuestion, related_name='boolean_selection', on_delete=models.CASCADE)
    is_true = models.BooleanField()

    def __str__(self):
        return f"{self.question.question_text} - {'Yes' if self.is_true else 'No'}"

    class Meta:
        db_table = 'fixed_boolean_selection'
        app_label = 'survey'