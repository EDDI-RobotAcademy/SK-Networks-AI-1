from srbcb.repository.srbcb_repository_impl import SrbcbRepositoryImpl
from srbcb.service.srbcb_service import SrbcbService


class SrbcbServiceImpl(SrbcbService):
    def __init__(self):
        self.srbcbRepository = SrbcbRepositoryImpl()

    def ruleBaseResponse(self, userSendMessage):
        return self.srbcbRepository.generateBotMessage(userSendMessage)

