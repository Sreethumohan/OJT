from textblob import TextBlob
text=[
"I Love NLP ! Its works great and i am very satisfied",
"This is my first experience on doing sewntiment analysis, I am little bit disappointed",
"The NLP sentiment analysis is quiet intresting"
]
def analyze_sentiment(text):
    analysis=TextBlob(text)
    polarity=analysis.sentiment.polarity
    if polarity>0:
        return "Positive"
    elif polarity<0:
        return "Negative"
    else:
        return "Neutral"
    return sentiment
for text in text:
    sentiment=analyze_sentiment(text)
    print(f"Text:{text}")
    print(f"sentiment:{sentiment}\n")