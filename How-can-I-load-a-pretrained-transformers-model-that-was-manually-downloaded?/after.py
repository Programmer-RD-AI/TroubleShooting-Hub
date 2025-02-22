from transformers import TFAutoModelForSequenceClassification, AutoTokenizer, pipeline

model = TFAutoModelForSequenceClassification.from_pretrained(
    "./models/twitter-roberta-base-sentiment-latest/"
)
tokenizer = AutoTokenizer.from_pretrained(
    "./models/twitter-roberta-base-sentiment-latest/"
)

# Note: Correct the task name spelling to "sentiment-analysis"
analyze = pipeline(task="sentiment-analysis", model=model, tokenizer=tokenizer)

print(analyze("this is good"))
print(analyze("this is bad"))
