import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (_, value) in data.items()]
yesterday_data = data_list[0]
yesterday_close_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = float(day_before_yesterday_data["4. close"])

difference = abs(yesterday_close_price - day_before_yesterday_close_price)

diff_percent = (difference / yesterday_close_price) * 100

if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_resp = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_resp.json()["articles"][:3]

    formatted_articles = [
        f"Headline: {article['title']}. \nBrief: {article['description']}"
        for article in articles
    ]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(
                body=article,
                from_=os.environ.get("TWILIO_FROM_NUMBER"),
                to=os.environ.get("TWILIO_TO_NUMBER")
            )
