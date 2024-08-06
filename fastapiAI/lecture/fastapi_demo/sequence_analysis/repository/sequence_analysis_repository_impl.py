import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer

from sequence_analysis.repository.sequence_analysis_repository import SequenceAnalysisRepository

preDefinedUserMessage = [
    "그저께 비가 왔다.",
    "어제 비가 왔다.",
    "오늘도 비가 왔다.",
    "내일도 비가 온다.",
    "모레도 비가 온다.",
    "이번주 내내 비가 온다.",
    "이번달 내내 비가 온다.",
    "일년 내내 비가 온다.",
    "10년간 비가 왔다.",
    "100년간 비가와서 잠겼다.",
]

class SequenceAnalysisRepositoryImpl(SequenceAnalysisRepository):
    def createTokenizer(self, userSendMessage):
        tokenizer = Tokenizer()
        # tokenizer.fit_on_texts(userSendMessage)
        tokenizer.fit_on_texts(preDefinedUserMessage)

        return tokenizer

    def extractSequence(self, tokenizer, userSendMessage):
        totalWords = len(tokenizer.word_index) + 1

        inputSequences = []

        # for line in userSendMessage:
        for line in preDefinedUserMessage:
            tokenList = tokenizer.texts_to_sequences([line])[0]
            for index in range(1, len(tokenList)):
                nGramSequence = tokenList[:index+1]
                inputSequences.append(nGramSequence)
                print(f"inputSequences: {inputSequences}")

