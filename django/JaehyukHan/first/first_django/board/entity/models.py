from django.db import models

# Create your models here.
# models.Model 이 적혀있는 부분이 실제로 Spring의 JPA와 같이
# DB query 생성 자동화를 지원하도록 서포트합니다.
class Board(models.Model):
    boardId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False)
    writer = models.CharField(max_length=32, null=False)
    content = models.TextField()
    # auto_now_add 는 추가하는 시점의 시간을 기록
    regDate = models.DateTimeField(auto_now_add=True)
    # auto_now 는 변경하는 시점의 시간을 기록
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # 테이블 이름을 Meta 지정 없이 사용할 경우
    # django가 자기 멋대로 요상한 이름의 테이블을 자동 생성합니다.
    # 그러므로 나는 꼭 이 명칭으로 테이블을 생성하고 싶다 하는 경우
    # Meta를 사용해서 테이블 이름을 지정하는 것이 좋습니다.
    # 주의 사항: DB 자체가 가지고 있는 내장 keyword 사용에 주의합시다.
    #          DB 내부의 키워드가 사용되면 django가 자동화를 하면서
    #          내부 데이터를 다 깨뜨리고 난리가 날 수 있습니다.
    class Meta:
        db_table = "board"