import spacy
from nltk import sent_tokenize, word_tokenize

from sentence_structure_analysis.repository.sentence_structure_analysis_repository import \
    SentenceStructureAnalysisRepository


class SentenceStructureAnalysisRepositoryImpl(SentenceStructureAnalysisRepository):


    def sentenceTokenize(self, text):
        print(f"repository -> sentenceTokenize(): {text}")
        return sent_tokenize(text)

    def wordTokenize(self, text):
        print(f"repository -> wordTokenize(): {text}")
        return word_tokenize(text)

    def sentenceAnalysis(self, text):
        englishLanguagePack = spacy.load("en_core_web_sm")
        document = englishLanguagePack(text)

        # 논문 분석을 위해선 latex의 syntax를 인식할 수 있게끔 바꿔야함
        for token in document:
            print(f"단어: {token.text}, 품사: {token.pos_}, 종속 관계: {token.dep_}, 부모 단어: {token.head.text}")

        return document