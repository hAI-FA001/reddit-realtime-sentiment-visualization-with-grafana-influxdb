import praw
import os
from dotenv import load_dotenv
from src.sentiment_analysis.sentiment_model import analyze_sentiment

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")


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

        print(f"Title: {title}")
        print(f"Sentiment: {analyze_sentiment(title)}")
        print(f"Text: {text}")
        print(f"Sentiment: {analyze_sentiment(text)}")
        print("-" * 50)


if __name__ == "__main__":
    subreddit = "DigitalSreeni"
    start(subreddit)
