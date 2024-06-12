from django.db import models
# models.py가 entity에 해당하므로 entity 디렉토리로 끌어오기
# Create your models here.

# 인식하려면 models.Model 을 상속받아야 함
# Spring의 jpa처럼 django에서도 우리가 db 쿼리를 직접 짜지 않아도 기능을 실행하도록 도움 (자동화)
# 그런 기능이 models.Model에서 지원함 >> "정보만 제대로 주면 내가 알아서 쿼리를 만든다."
class Board(models.Model):
    # 쿼리 대신 이렇게 class type으로 실행시키면 만들어짐
    boardId = models.AutoField(primary_key=True) # AutoField == AutoIncrement 적용
    title = models.CharField(max_length=128, null=False) # 숫자 잘못 입력했을 때 숫자만 바꿔도 알아서 업뎃 됨
    writer = models.CharField(max_length=32, null=False)
    content = models.TextField() # 문자가 긴 경우 TextField 적용
    regDate = models.DateTimeField(auto_now_add=True) # 추가된 현재시간 적용
    updDate = models.DateTimeField(auto_now=True) # 변경된 현재시간 적용

    def __str__(self):
        return self.title

    # 테이블 이름을 Meta 지정 없이 사용할 경우
    # django가 자기 멋대로 요상한 이름의 테이블을 자동 생성합니다.
    # 그러므로 나는 꼭 이 명칭으로 테이블을 생성하고 싶다 하는 경우
    # Meta를 사용해서 테이블 이름을 지정하는 것이 좋다.
    # 주의사항 : DB자체가 가지고 있는 내장 Keyword 사용에 주의 합시다
    #          DB 내부의 키워드가 사용되면 django가 자동화를 하면서 내부 데이터를 다 깨뜨릴 수 있음
    class Meta:
        db_table = 'board'
