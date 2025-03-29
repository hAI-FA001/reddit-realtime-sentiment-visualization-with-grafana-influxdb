from textblob import TextBlob


def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity


if __name__ == "__main__":
    text = "This is a great day!"
    print(f'Sentiment for "{text}": {analyze_sentiment(text)}')
