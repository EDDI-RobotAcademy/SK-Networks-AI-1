from django.db import models
from account.entity.account import Account


class Report(models.Model):
    reportId = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='reports')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=3)

    def __str__(self):
        return f"Report -> id: {self.reportId}, account: {self.account.id}"

    class Meta:
        db_table = 'report'
        app_label = 'report'