from transformers import BertTokenizer, BertForSequenceClassification

from transition_learning.repository.transition_learning_repository import TransitionLearningRepository


class TransitionLearningRepositoryImpl(TransitionLearningRepository):
    MODEL_NAME_BERT_BASE_UNCASED = 'bert-base-uncased'

    def prepareBertBaseUncasedLearningSet(self):
        tokenizer = BertTokenizer.from_pretrained(self.MODEL_NAME_BERT_BASE_UNCASED)
        model = BertForSequenceClassification.from_pretrained(self.MODEL_NAME_BERT_BASE_UNCASED, num_labels = 2)

        return self.MODEL_NAME_BERT_BASE_UNCASED, tokenizer, model