from transformers import pipeline
myPipe = pipeline(
    'text-classification',
    model = 'distilbert-base-uncased-finetuned-sst-2-english'
)

print(myPipe('I hate school so much it absolutely sucks'))
