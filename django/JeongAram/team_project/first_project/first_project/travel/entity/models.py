from django.db import models

class Travel(models.Model):
    travelId = models.AutoField(primary_key=True)
    travelName = models.CharField(max_length=128, null=False)
    travelLocation = models.CharField(max_length=32, null=False)
    travelProperty = models.TextField()
    travelContent = models.TextField()
    travelImage = models.CharField(max_length=100, null=True)


    # 추후 이미지 관련 필드 추가
    registeredDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.travelName

    class Meta:
        db_table = 'travel'
