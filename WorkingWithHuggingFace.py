from transformers import pipeline

userInput = input('Enter a sentence to get run: ')

sentiment = pipeline(
    'text-classification',
    model = 'distilbert-base-uncased-finetuned-sst-2-english'
)


grammar = pipeline(
    task = 'text-classification', 
    model = 'abdulmatinomotoso/English_Grammar_Checker'
)

print(grammar(userInput))
print(sentiment(userInput))
