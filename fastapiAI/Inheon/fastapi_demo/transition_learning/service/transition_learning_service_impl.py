import torch

from transition_learning.repository.transition_learning_repository_impl import TransitionLearningRepositoryImpl
from transition_learning.service.transition_learning_service import TransitionLearningService


class TransitionLearningServiceImpl(TransitionLearningService):
    def __init(self):
        self.__transitionLearningRepository = TransitionLearningRepositoryImpl()

    def predictText(self, transitionLearningPredictRequestForm):
        modelName, tokenizer, model = self.__transitionLearningRepository.prepareLearningSet()
        model.eval()

        tokenizedUserInputText = tokenizer(
            transitionLearningPredictRequestForm.firstSentence,
            transitionLearningPredictRequestForm.secondSentence,
            return_tensors='pt',
            truncation=True,
        )

        with torch.no_grad():
            outputList = model(**tokenizedUserInputText)
            logitList = outputList.logits
            prediction = torch.argmax(logitList, dim=-1).item()

        if prediction == 1:
            result = '두 문장은 다르지만 의미는 같습니다.'
        else:
            result = '두 문장의 의미는 다릅니다.'

        return result