import praw
import os
from dotenv import load_dotenv
from src.sentiment_analysis.sentiment_model import analyze_sentiment
from src.data_storage.influxdb import write_to_db

load_dotenv(override=True)

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

SUBREDDIT = os.getenv("SUBREDDIT")


def start(subreddit):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
    )

    subreddit = reddit.subreddit(subreddit)

    for submission in subreddit.stream.submissions():
        title = submission.title
        text = submission.selftext

        title_sentiment = analyze_sentiment(title)
        text_sentiment = analyze_sentiment(text)

        write_to_db(title, title_sentiment, text, text_sentiment)

        print(f"Title: {title}")
        print(f"Sentiment: {title_sentiment}")
        print(f"Text: {text}")
        print(f"Sentiment: {text_sentiment}")
        print("-" * 50)


if __name__ == "__main__":
    start(SUBREDDIT)
