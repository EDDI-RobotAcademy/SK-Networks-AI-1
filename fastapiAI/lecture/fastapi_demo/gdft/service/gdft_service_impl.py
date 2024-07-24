import tensorflow
import torch

from gdft.repository.gdft_repository_impl import GDFTRepositoryImpl
from gdft.service.gdft_service import GDFTService




class GDFTServiceImpl(GDFTService):
    def __init__(self):
        self.gdftRepository = GDFTRepositoryImpl()

    def gdftTest(self):
        tokenizer = self.gdftRepository.acquireTokenFromPretrainedModel()
        model = self.gdftRepository.acquireModelFromPretrainedModel()

        needToTrainDataset = self.gdftRepository.loadDataset(tokenizer)
        # dataCollator = self.gdftRepository.configDataCollator(tokenizer)

        trainingParameter = self.gdftRepository.configTrainingParameter()
        trainer = self.gdftRepository.configTrainer(model, trainingParameter, needToTrainDataset, tokenizer)

        self.gdftRepository.trainFineTuning(trainer)

        # optimizer = tensorflow.keras.optimizers.Adam(learning_rate=3e-5)
        # model.compile(optimizer=optimizer, loss=model.compute_loss)
        # model.fit(needToTrainDataset, epochs=3)

        model.save_pretrained("./game_fine_tuned_model")
        tokenizer.save_pretrained("./game_fined_tuned_model")

    def gdftUserRequestTest(self, text):
        print(f"service -> gdftUserRequestTest()")

        tokenizer = self.gdftRepository.acquireTokenFromPretrainedModel()
        model = self.gdftRepository.acquireModelFromPretrainedModel()

        # inputIds = self.gdftRepository.encodeTokenizer(tokenizer, text)
        #
        # with torch.no_grad():
        #     output = self.gdftRepository.generateText(model, inputIds)
        #
        # response = self.gdftRepository.decodeTokenizer(tokenizer, output)

        inputList = tokenizer.encode_plus(text, return_tensors="pt", padding=True)
        inputIdList = inputList['input_ids']
        attentionMask = inputList['attention_mask']

        with torch.no_grad():
            output = model.generate(inputIdList, attention_mask=attentionMask, max_length=200, num_return_sequences=1, pad_token_id=tokenizer.pad_token_id)

        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return {"response": response}

