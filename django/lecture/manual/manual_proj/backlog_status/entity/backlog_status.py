from django.db import models

from backlog.entity.backlog import Backlog
from backlog_status.entity.backlog_status_type import BacklogStatusType


class BacklogStatus(models.Model):
    status = models.IntegerField(
        choices=BacklogStatusType.choices(),
        default=BacklogStatusType.BACKLOG.value
    )
    backlog = models.ForeignKey('backlog.Backlog', on_delete=models.CASCADE, related_name='statuses')

    def __str__(self):
        return f"{self.backlog.title} - {BacklogStatusType(self.status).name.lower()}"

    class Meta:
        db_table = 'backlog_status'
