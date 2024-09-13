from django.db import models
from .survey import Survey
from .survey_question import SurveyQuestion
from .fixed_five_score_selection import FixedFiveScoreSelection
from .fixed_boolean_selection import FixedBooleanSelection

class SurveyAnswer(models.Model):
    survey = models.ForeignKey(Survey, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    five_score_selection = models.ForeignKey(FixedFiveScoreSelection, blank=True, null=True, on_delete=models.SET_NULL)
    boolean_selection = models.ForeignKey(FixedBooleanSelection, blank=True, null=True, on_delete=models.SET_NULL)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer to {self.question.question_text}"

    class Meta:
        db_table = 'survey_answer'
        app_label = 'survey'