from django.db import models

class Travel(models.Model):
    travelId = models.AutoField(primary_key=True) # AutoField == AutoIncrement 적용
    travelName = models.CharField(max_length=128, null=False) #
    travelLocation = models.CharField(max_length=32, null=False)
    travelProperty = models.TextField() # 문자가 긴 경우 TextField 적용
    travelContent = models.TextField()
    travelImage = models.CharField(max_length=100, null=False)

    def __str__(self): # 애매함
        return self.travelName

    class Meta:
        db_table = 'travel'