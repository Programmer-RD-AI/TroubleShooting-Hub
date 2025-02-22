from transformers import pipeline, TFPreTrainedModel, AutoTokenizer
import os

dir = "./models/twitter-roberta-base-sentiment-latest/"
print(os.listdir(dir))  # confirm the folder contents

model = TFPreTrainedModel.from_pretrained(dir)
tokenizer = AutoTokenizer.from_pretrained(dir)

analyze = pipeline(task="sentiment-analyis", model=model, tokenizer=tokenizer)
print(analyze("this is good"))
print(analyze("this is bad"))
