from transformers import GPT2Tokenizer, DataCollatorForLanguageModeling, TrainingArguments, GPT2LMHeadModel, Trainer

from gdft.repository.gdft_repository import GDFTRepository

from datasets import Dataset

import tensorflow as tf

gameRules = [
    "광역기는 배틀 필드에 나와 있는 모든 유닛을 공격 할 수 있습니다.",
    "단일기는 배틀 필드에 있는 특정 유닛을 공격 할 수 있습니다.",
    "네더 블레이드는 매턴 광역기와 단일기를 사용합니다.",
    "네더 블레이드의 광역기는 10의 피해를 줍니다.",
    "네더 블레이드는 단일기는 20의 피해를 줍니다.",
    "광역기는 한 번에 여러 유닛을 공격 할 수 있는 능력입니다.",
    "단일기는 특정 유닛을 목표로 삼아 공격하는 능력입니다."
    "유닛은 공격을 할 수 있습니다."
]


class GDFTRepositoryImpl(GDFTRepository):
    MODEL_NAME = "gpt2"

    def acquireTokenFromPretrainedModel(self):
        tokenizer = GPT2Tokenizer.from_pretrained(self.MODEL_NAME)
        tokenizer.pad_token = tokenizer.eos_token

        return tokenizer

    def acquireModelFromPretrainedModel(self):
        return GPT2LMHeadModel.from_pretrained(self.MODEL_NAME)

    def loadDataset(self, tokenizer):
        BLOCK_SIZE = 128
        encodedData = tokenizer("\n\n".join(gameRules), return_tensors="pt", padding=True, truncation=True, max_length=BLOCK_SIZE)
        dataset = Dataset.from_dict({
            'input_ids': encodedData['input_ids'],
            'attention_mask': encodedData['attention_mask'],
            'labels': encodedData['input_ids']
        })

        return dataset

    def configDataCollator(self, tokenizer):
        return DataCollatorForLanguageModeling(
            tokenizer=tokenizer,
            mlm=False
        )

    def configTrainingParameter(self):
        return TrainingArguments(
            output_dir="./results",
            overwrite_output_dir=True,
            num_train_epochs=1000,
            per_device_train_batch_size=2,
            save_steps=10_000,
            save_total_limit=2,
        )

    def configTrainer(self, model, trainingParameter, needToTrainDataset, tokenizer):
        return Trainer(
            model=model,
            args=trainingParameter,
            # data_collator=dataCollator,
            train_dataset=needToTrainDataset,
            tokenizer=tokenizer
        )

    def trainFineTuning(self, trainer):
        trainer.train()

    def encodeTokenizer(self, tokenizer, text):
        return tokenizer.encode(text, return_tensors="pt", padding=True)

    def generateText(self, model, inputIds):
        return model.generate(inputIds, max_length=200, num_return_sequences=1)

    def decodeTokenizer(self, tokenizer, output):
        return tokenizer.decode(output[0], skip_special_tokens=True)





