from srbcb.repository.srbcb_repository import SrbcbRepository

fixedResponseList = {
    "hi": "안녕! 오늘은 무엇을 도와줄까 ?",
    "hello": "I'm fine and you ?",
    "bye": "잘가!",
}

class SrbcbRepositoryImpl(SrbcbRepository):
    def generateBotMessage(self, message):
        lowerMessage = message.lower()
        return fixedResponseList.get(lowerMessage, "미안해! 무슨 애긴지 모르겠어!")