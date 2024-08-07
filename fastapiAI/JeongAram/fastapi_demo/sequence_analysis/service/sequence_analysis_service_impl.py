from sequence_analysis.repository.sequence_analysis_repository_impl import SequenceAnalysisRepositoryImpl
from sequence_analysis.service.sequence_analysis_service import SequenceAnalysisService


class SequenceAnalysisServiceImpl(SequenceAnalysisService):
    def __init__(self):
        self.sequenceAnalysisRepository = SequenceAnalysisRepositoryImpl()

    def predictNextSequence(self, userSendMessage):
        tokenizer = self.sequenceAnalysisRepository.createTokenizer(userSendMessage)
        totalWords, inputSequences = self.sequenceAnalysisRepository.extractSequence(tokenizer, userSendMessage)

        maxSequenceLength = max([len(x) for x in inputSequences])

        paddedInputSequences = self.sequenceAnalysisRepository.paddingSequence(inputSequences, maxSequenceLength)
        X, y = self.sequenceAnalysisRepository.separateInputAndOutputSequences(paddedInputSequences, totalWords)
        trainedModel = self.sequenceAnalysisRepository.trainSequence(totalWords, maxSequenceLength, X, y)

        generatedText = self.sequenceAnalysisRepository.generateText(
            "오늘도", 2, trainedModel, maxSequenceLength, tokenizer)

        return generatedText





