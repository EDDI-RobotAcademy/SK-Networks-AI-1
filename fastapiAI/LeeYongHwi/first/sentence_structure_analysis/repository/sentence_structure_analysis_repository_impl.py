import spacy
from nltk import sent_tokenize, word_tokenize

from sentence_structure_analysis.repository.sentence_structure_analysis_repository import \
    SentenceStructureAnalysisRepository


class SentenceStructureAnalysisRepositoryImpl(SentenceStructureAnalysisRepository):
    def sentenceTokenize(self, text):
        return sent_tokenize(text)

    def wordTokenize(self, text):
        return word_tokenize(text)

    def sentenceAnalysis(self, text):
        englishLanguagePack = spacy.load("en_core_web_sm")
        document = englishLanguagePack(text)


        # NOUN: 명사
        # PRON: 대명사
        # VERB: 동사
        # ADJ: 형용사
        # ADV: 부사
        # DET: 한정사
        # PART: 조사
        # AUX: 조동사
        # CONJ: 접속사
        # Punct: 구두점
        # SCONJ: 종속 접속사
        # PROPN: 고유 대명사
        for token in document:
            print(f"단어: {token.text}, 품사: {token.pos_}, 종속 관계: {token.dep_}, 부모 단어: {token.head.text}")

        return document


