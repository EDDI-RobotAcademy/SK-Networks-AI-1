from sentence_structure_analysis.repository.sentence_structure_analysis_repository_impl import \
    SentenceStructureAnalysisRepositoryImpl
from sentence_structure_analysis.service.sentence_structure_analysis_service import SentenceStructureAnalysisService


class SentenceStructureAnalysisServiceImpl(SentenceStructureAnalysisService):
    def __init__(self):
        self.sentenceStructureAnalysisRepository = SentenceStructureAnalysisRepositoryImpl()

    def sentenceTokenize(self, sentenceRequest):
        return self.sentenceStructureAnalysisRepository.sentenceTokenize(sentenceRequest.toSentence())

    def wordTokenize(self, sentenceRequest):
        return self.sentenceStructureAnalysisRepository.wordTokenize(sentenceRequest.toSentence())

    def sentenceAnalysis(self, sentenceRequest):
        document = self.sentenceStructureAnalysisRepository.sentenceAnalysis(sentenceRequest.toSentence())

        result = []
        for token in document:
            result.append({
                "text": token.text,
                "pos": token.pos_,
                "dep": token.dep_,
                "head_text": token.head.text
            })

        return result

