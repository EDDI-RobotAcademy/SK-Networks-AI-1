from srbcb.repository.srbcb_repository import SrbcbRepository

fixedResponseList = {
    "hi": "안녕! 오늘은 무엇을 도와줄까 ?",
    "hello": "응 안녕! 무슨 일이야 ?",
    "bye": "잘가!",
}
class SrbcbRepositoryImpl(SrbcbRepository):
    def generateBotMessage(self, message):
        lowerMessage = message.lower()
        return fixedResponseList.get(lowerMessage, "미안해! 뭐라는지 모르겠어!")
