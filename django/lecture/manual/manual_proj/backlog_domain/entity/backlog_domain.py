from django.db import models

from backlog.entity.backlog import Backlog


class BacklogDomain(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=255, null=True, blank=True)
    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE, related_name='domains')

    def __str__(self):
        return f"{self.domain} (Backlog ID: {self.backlog.id})"

    class Meta:
        db_table = 'backlog_domain'
