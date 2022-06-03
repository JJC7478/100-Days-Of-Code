import os
import requests
from twilio.rest import Client
import html

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

AV_API_KEY = os.environ.get("AV_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

ACCT_SID = "AC6801ee7852237e37d558bd7618c33190"
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

TWIL_NUMBER = os.environ.get("TWIL_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")

client = Client(ACCT_SID, AUTH_TOKEN)

UP_SYMBOL = "🔺"
DOWN_SYMBOL = "🔻"

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": AV_API_KEY
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
daily_stock_data = stock_data["Time Series (Daily)"]
daily_list = [{day: value} for (day,value) in daily_stock_data.items()]
  

yesterday = [daily_list[0].get(key) for key in daily_list[0]]
yesterday_close = float(yesterday[0]["4. close"])
two_day = [daily_list[1].get(key) for key in daily_list[1]]
two_day_close = float(two_day[0]["4. close"])
diff = round((yesterday_close - two_day_close),2)
abs_diff = abs(diff)
percent_diff = round(abs(((yesterday_close-two_day_close)/yesterday_close) * 100),2)


if percent_diff > 5:
    if diff > 0:
        percent_message = f"{STOCK_NAME}: {UP_SYMBOL}{percent_diff}%"
    else:
        percent_message = f"{STOCK_NAME}: {DOWN_SYMBOL}{percent_diff}%"
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_articles = news_data["articles"]
    top_three = news_articles[:3]
    top_articles = [{"title": article["title"], "brief": article["description"]} for article in top_three]
    for article in top_articles:
        message = client.messages \
                        .create(
                            body=f"""
                            {percent_message} 
Headline: {html.unescape(article["title"])} 
Brief: {html.unescape(article["brief"])}""",
                            from_=TWIL_NUMBER,
                            to=MY_NUMBER
                        )

        print(message.status)



