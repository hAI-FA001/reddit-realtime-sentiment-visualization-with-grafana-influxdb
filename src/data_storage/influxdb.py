from influxdb_client_3 import InfluxDBClient3, Point, WritePrecision
import os
import datetime
from dotenv import load_dotenv

load_dotenv(override=True)

INFLUXDB_HOST = os.getenv("INFLUXDB_HOST")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUXDB_ORG = os.getenv("INFLUXDB_ORG")
INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET")


def write_to_db(title, title_sentiment, text, text_sentiment):
    client = InfluxDBClient3(
        host=INFLUXDB_HOST,
        token=INFLUXDB_TOKEN,
        org=INFLUXDB_ORG,
    )

    point = (
        Point("reddit_sentiment")
        .tag("title", title)
        .field("title_sentiment", title_sentiment)
        .field("text", text)
        .field("text_sentiment", text_sentiment)
        .time(datetime.datetime.now(datetime.UTC), WritePrecision.NS)
    )

    client.write(database=INFLUXDB_BUCKET, record=point)
    client.close()


if __name__ == "__main__":
    write_to_db("Test title", 0.123, "Test text", 0.456)
    print("Wrote data to InfluxDB")
