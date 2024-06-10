from django.db import models

class Product(models.Model):
    productId = models.AutoField(primary_key=True)    # AutoField : AutoIncrement 적용
    productName = models.CharField(max_length=128, null=False)
    price = models.CharField(max_length=32, null=False)
    content = models.TextField()    # 문자의 길이가 길어서 제한하기 어려울 때
    regDate = models.DateTimeField(auto_now_add=True)   # 등록 시간 자동으로 기록
    updDate = models.DateTimeField(auto_now=True)   # 변경 시간 자동으로 기록

    def __str__(self):
        return self.productName

    # 테이블 이름을 Meta 지정
    class Meta:
        db_table = 'product'
