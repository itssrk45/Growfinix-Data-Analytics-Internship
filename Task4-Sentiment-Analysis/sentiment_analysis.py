import pandas as pd
from textblob import TextBlob

df = pd.read_csv("reviews.csv")

def get_sentiment(review):
    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(get_sentiment)

print(df)

df.to_csv("sentiment_results.csv", index=False)

print("Sentiment Analysis Completed!")