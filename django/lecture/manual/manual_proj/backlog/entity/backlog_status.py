from django.db import models

from backlog.entity.backlog_status_type import BacklogStatusType


class BacklogStatus(models.Model):
    status = models.IntegerField(
        choices=BacklogStatusType.choices(),
        default=BacklogStatusType.OPEN.value  # Default to OPEN
    )
    backlog = models.ForeignKey('Backlog', on_delete=models.CASCADE, related_name='statuses')

    def __str__(self):
        return f"{self.backlog.title} - {BacklogStatusType(self.status).name.lower()}"  # Converts the status back to string for display

    class Meta:
        db_table = 'backlog_status'
        app_label = 'backlog'
