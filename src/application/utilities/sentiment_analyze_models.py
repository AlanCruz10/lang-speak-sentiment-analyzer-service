from transformers import pipeline

model_multilingual = "nlptown/bert-base-multilingual-uncased-sentiment"
analytic_sentiments_multilingual = pipeline("sentiment-analysis", model=model_multilingual)