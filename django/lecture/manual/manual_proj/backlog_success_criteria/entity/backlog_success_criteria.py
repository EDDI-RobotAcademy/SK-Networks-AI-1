from django.db import models

from backlog.entity.backlog import Backlog


class BacklogSuccessCriteria(models.Model):
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE, related_name='success_criteria')
    success_criteria = models.TextField()

    def __str__(self):
        return f"Criteria for {self.backlog.title}: {self.success_criteria}"

    class Meta:
        db_table = 'backlog_success_criteria'
