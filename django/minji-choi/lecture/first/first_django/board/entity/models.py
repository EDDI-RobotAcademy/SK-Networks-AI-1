from django.db import models

# Create your models here.
# models.Model이 적혀있는 부분이 실제로 Spring의 JPA와 같이 DB query 생성 자동화를 지원하도록 서포트함
class Board(models.Model):
    # 게시물 DB
    boardId = models.AutoField(primary_key=True) # AutoFiled : autoIncrement가 적용되는 것
    title = models.CharField(max_length=128, null=False) # 문자열 값
    writer = models.CharField(max_length=32, null=False) # 작성자
    content = models.TextField() # 문자 길이를 제한하기 어려운 경우. 글 내용
    regDate = models.DateTimeField(auto_now_add=True) # 등록일자. 등록되는 즉시의 시점
    upDate = models.DateTimeField(auto_now=True) # 변경하는 즉시

    def __str__(self):
        return self.title

    # 테이블 이름을 meta 지정없이 사용할 경우
    # django가 자기 멋대로 이상한 이름의 테이블을 자동 생성합니다.
    # 그러므로 꼭 이 명칭으로 테이블을 생성해야 하는 경우 meta를 사용 해서 테이블 이름을 지정하는 것이 좋다.
    # **주의 사항** DB 자체가 가지고 있는 내장 keyword 사용에 주의합니다.
    # DB 내부의 키워드가 사용되면 django가 자동화를 하면서 내부 데이터를 다 깨뜨리고 난리난리~~난다


    class Meta:
        db_table = 'board'
    # 장고가 default로 사용하는 DB가 sqlite3