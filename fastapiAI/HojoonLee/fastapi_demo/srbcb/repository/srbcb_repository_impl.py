from srbcb.repository.srbcb_repository import SrbcbRepository

# 여기에 미리 지정된 rule의 입력에 대해서만 답을 받아주고
# 만약 여기 의외의 message가 온다면 default로 무슨 얘긴지 모르겠다는 말이 나오게 된다.
fixedResponseList = {
    "hi" : "안녕! 오늘은 무엇을 도와줄까 ?",
    "hello": "응 안녕! 무슨 일이야 ?",
    "bye": "잘가!",
}

class SrbcbRepositoryImpl(SrbcbRepository):
    def generateBotMessage(self, userSendMessage):
        lowerMessage = userSendMessage.lower() # 소문자화
        return fixedResponseList.get(lowerMessage, "미안해! 무슨 얘긴지 모르겠어!")