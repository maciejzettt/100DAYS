import dotenv
import os
import requests
import datetime
import print_dict
import news

def format_info(info_text: str, caption='Information') -> str:
    return f"\033[38;5;220m\033[48;5;238m{caption}:\033[0m\033[38;5;189m {info_text} \033[0m"

DIR = os.path.dirname(__file__)
dotenv.load_dotenv(os.path.join(DIR, "auth.pwd"))

ONE_DAY =  datetime.timedelta(days=1)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_AUTH = os.environ.get("AV_API_KEY")

NEWSAPI_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWSAPI_AUTH = os.environ.get("NEWSAPI_KEY")

av_params = {
    "apikey": AV_AUTH,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
}

av_resp_raw = requests.get(url=AV_ENDPOINT, params=av_params)
av_resp_raw.raise_for_status()
print(f"AV RESPONSE: {av_resp_raw.status_code}")

today = datetime.date.today()
last_day = today - ONE_DAY
penultimate_day = last_day - ONE_DAY

av_data = dict(av_resp_raw.json()).get("Time Series (Daily)")
av_data_last_day = av_data.get(str(last_day))

while av_data_last_day is None:
    last_day = last_day - ONE_DAY
    penultimate_day = penultimate_day - ONE_DAY
    av_data_last_day = av_data.get(str(last_day))
    
av_data_penultimate_day = av_data.get(str(penultimate_day))
while av_data_penultimate_day is None:
    penultimate_day = penultimate_day - ONE_DAY
    av_data_penultimate_day = av_data.get(str(penultimate_day))
    
print(last_day, penultimate_day)

print(f"\nDATA FOR {last_day}:")
print_dict.print_dict(av_data_last_day)
print(f"\nDATA FOR {penultimate_day}:")
print_dict.print_dict(av_data_penultimate_day)

last_day_close = float(av_data_last_day.get("4. close"))
penultimate_day_close = float(av_data_penultimate_day.get("4. close"))

price_diff = abs(last_day_close - penultimate_day_close)
price_change_direction = "RISE" if last_day_close >= penultimate_day_close else "FALL"
price_diff_percent = price_diff / penultimate_day_close * 100
print(format_info(f"CHANGE IN PRICE: {price_diff_percent:.2f}% [USD {price_diff:.4f}] {price_change_direction}.", "TSLA"))

if price_diff_percent >= 5:
    tesla_news = news.NewsAPIHeadlines(NEWSAPI_AUTH)
    print("The following articles have been found:")
    while (tesla_news.has_news()):
        article = tesla_news.get_next_headline()
        print(f"\nArticle by {article.get('author')} published on {article.get('publishedAt')}")
        print(f"TITLE: {article.get('title')}")
        print(f"DESCRIPTION: {article.get('description')}")
else:
    print("No news will be provided")

