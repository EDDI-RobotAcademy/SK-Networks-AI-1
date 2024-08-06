from sequence_analysis.repository.sequence_analysis_repository_impl import SequenceAnalysisRepositoryImpl
from sequence_analysis.service.sequence_analysis_service import SequenceAnalysisService


class SequenceAnalysisServiceImpl(SequenceAnalysisService):
    def __init__(self):
        self.sequenceAnalysisRepository = SequenceAnalysisRepositoryImpl()

    def predictNextSequence(self, userSendMessage):
        print(f"service -> predictNextSequence(): userSendMessage: {userSendMessage}")

        tokenizer = self.sequenceAnalysisRepository.createTokenizer(userSendMessage)
        self.sequenceAnalysisRepository.extractSequence(tokenizer, userSendMessage)

        return None